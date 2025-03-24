from pydantic import BaseModel,EmailStr

class Users(BaseModel):
    userId:int
    username:str
    email:EmailStr
    password:str