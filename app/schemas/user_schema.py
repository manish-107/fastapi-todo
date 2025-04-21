# Pydantic models that define the structure of data before saving it to the database. These models help validate and ensure data consistency when interacting with MongoDB.

from pydantic import BaseModel,EmailStr

class Users(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:str

class SigniRequest(BaseModel):
    email:EmailStr
    password:str

class TodoResponse(BaseModel):
    todo_title:str
    todo_desc:str