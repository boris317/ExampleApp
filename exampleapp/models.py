from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

import logging
log = logging.getLogger(__name__)

Base = declarative_base()
DBSession = scoped_session(sessionmaker())

def init_db(engine):
    DBSession.configure(bind=engine)    
    Base.metadata.create_all(bind=engine)
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(256))