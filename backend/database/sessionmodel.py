from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy import func
from backend.database.db import Base

class Chat_Session(Base):
    __tablename__ = 'session'

    id = Column(Integer, primary_key= True)

    session_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now() )


    message = relationship('User_chat', back_populates='session', cascade="all, delete-orphan")



    




