from sqlalchemy import Integer, Column, Text, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func, ForeignKey
from database.db import Base
from database.sessionmodel import Chat_Session

class User_Chat(Base):

    __tablename__ = 'user_chat'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(100), index = True, nullable= False)

    topic = Column(String(500), nullable = False)
    action = Column(String(100), nullable = True)

    raw_text = Column(Text, nullable=False)
    extracted_data = Column(Text, nullable=True)
    status = Column(String(50), nullable= False)


    interaction_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    session_id = Column(Integer, ForeignKey = (Chat_Session.id), nullable=False)

    session = relationship('Chat_session',  back_populates='message')




    