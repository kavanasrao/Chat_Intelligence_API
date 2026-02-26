from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os 
from backend.core.config import Config

database_uri = Config.get('DATABASE_URI')
engine = create_engine(database_uri)


SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)


Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


