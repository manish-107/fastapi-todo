from sqlalchemy import Integer, String, DateTime, func, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(60), nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)

    role = relationship("Roles", back_populates="user", uselist=False)
    todos = relationship("Todos",back_populates="user")

class Roles(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    user = relationship("Users", back_populates="role")


class Todos(Base):
    __tablename__ = "todos"

    todo_id = Column(Integer,primary_key=True,autoincrement=True)
    todo_title = Column(String(50),nullable=False)
    todo_desc = Column(String)
    create_date = Column(DateTime,default=func.now())

    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False) 

    user = relationship("Users",back_populates="todos")