from .db import Base, engine
from  . import sessionmodel, usermodel
   


def init__db() :
    Base.metadata.create_all(bind = engine)