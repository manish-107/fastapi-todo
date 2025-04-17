from sqlalchemy import Integer,String,DateTime,func,Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(60),nullable=False)
    email = Column(String,unique=True)
    password = Column(String,nullable=True)