# Pydantic models that define the structure of data before saving it to the database. These models help validate and ensure data consistency when interacting with MongoDB.

from pydantic import BaseModel,EmailStr

class Users(BaseModel):
    name:str
    age:int
    email:EmailStr
    password:str