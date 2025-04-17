# Pydantic models for request validation and response shaping in FastAPI.
from pydantic import EmailStr,BaseModel,Field
from typing import Optional

class UserModel(BaseModel):
    name:str = Field(...,min_length=0,max_length=50)
    age:Optional[int] = Field(None , ge=18, le=99)
    email:EmailStr 
    password:str = Field(..., min_length=6, max_length=20)

