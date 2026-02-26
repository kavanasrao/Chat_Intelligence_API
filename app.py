from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, field_validator
from sqlalchemy.orm import Session

from backend.database import  init__
from backend.database.db import get_db
from backend.database.usermodel import User_Chat

from backend.agent.state import AgentState
from backend.agent.graph import build_graph


import logging 

graph = build_graph()

app = FastAPI()


@app.on_event('startup')
def start_db():
    init__.init__db()

logger = logging.getLogger(__name__)

class ChatInput(BaseModel):
    message : str

    @field_validator('message')
    def field_validate(self, value):
        if not value.strip():
            raise ValueError('Message can not be empty!')
        
        elif len(value) > 2000:
            raise ValueError('The input length exceeded') 
        
        return value.strip()
    

@app.post('/analyse')
def chat_interaction(data : ChatInput, db: Session = Depends(get_db)):
    
    try :
        state = AgentState(raw_text=data.message)
        result = graph.invoke(state)

    except Exception as e :
        logger.exception('Graph Processing Failed')
        raise HTTPException(status_code= 500, detail= 'processing failed')

    extracted = result.extracted_text

    chat = User_Chat(
        name = extracted.get('client_name'),
        topic = extracted.get('topic'),
        action = extracted.get('action'), 
        raw_text = result.raw_text,
        status = result.status

    )

    try : 
        db.add(chat)
        db.commit()
        db.refresh(chat)
        logger.info('Data added to database')
    
    except Exception : 
        db.rollback()
        logger.exception('Database insert failed')
        raise HTTPException(status_code= 500, detail= ' Failed to insert Db')

    return result
    


@app.get('/Interaction')
def all_records(db : Session = Depends(get_db)):

   
    record = db.query(User_Chat).all()
    if not record:
        logger.exception("Information not found")
        raise HTTPException(status_code=404, detail='Not found')
    
    
    return record
    


@app.get('/Interaction/{id}')
def record_id(id : int, db : Session = Depends(get_db)):
        
    record = db.query(User_Chat).filter(User_Chat.id == id).first()
    if not record:
        logger.exception('Record not found')
        raise HTTPException(status_code= 404, detail='Record not found')
    
    return record
    



@app.get('/analytics')
def analytics(db : Session = Depends(get_db)):

    try :
        total = db.query(User_Chat).count()
        done = db.query(User_Chat).filter(User_Chat.status == 'done').count()
        failed = db.query(User_Chat).filter(User_Chat.status != 'done').count()
    
    except Exception:
        raise HTTPException(status_code= 500, detail='Could not calculate analytics')

    return {
        'total' : total,
        'done' : done,
        'failed' : failed
    }



@app.get('/health')
def health_check():
    return {'status' : 'OK'}


