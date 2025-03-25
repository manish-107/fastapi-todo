from app.database import user_collection
from fastapi import HTTPException
from app.models.user_model import UserModel
from pydantic import EmailStr
from typing import Optional

class UserService:

    @staticmethod   
    async def get_all_users() -> list:
        users = await user_collection.find().to_list(length=None)

        if not users:
            raise HTTPException(status_code=404,detail="No Users found")
        
        for user in users:
            user["_id"] = str(user["_id"])
            
        return users
    
    @staticmethod
    async def get_userby_email(email:EmailStr) -> Optional[dict]: 
        user = await user_collection.find_one({"email":email})
        if user:
            user["_id"] = str(user["_id"])
            return user
        
        return None
    
    @staticmethod
    async def create_user(user:UserModel):
        user_dict = user.model_dump() 
        existing_user =  await UserService.get_userby_email(user.email)
        
        if existing_user:
            raise HTTPException(status_code=400, detail="User email already exists")

        result = await user_collection.insert_one(user_dict)
        
        if not result.inserted_id:
            raise HTTPException(status_code=404,detail="Unable to create user")
        
        return result
    
   


