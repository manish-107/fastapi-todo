from app.database import user_collection
from fastapi import HTTPException
from app.models.models import UserModel
from pydantic import EmailStr
from typing import Optional
from app.schemas.user_schema import SigniRequest
from datetime import timedelta
from app.services.auth_service import hash_password,verify_password,create_access_token

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

        user_dict["password"] = hash_password(user.password)

        print(user_dict)

        result = await user_collection.insert_one(user_dict)
        
        if not result.inserted_id:
            raise HTTPException(status_code=404,detail="Unable to create user")
        
        return result
    
    @staticmethod
    async def signin_user(user:SigniRequest):
        user_dict = user.model_dump()

        existing_user =  await UserService.get_userby_email(user_dict["email"])

        if not existing_user:
            raise HTTPException(status_code=404, detail="User does not exist")

        if not verify_password(user_dict["password"], existing_user["password"]):
            raise HTTPException(status_code=401, detail="Incorrect password")

        access_token = create_access_token(data={"sub": existing_user["email"], "user_id": str(existing_user["_id"])},
            expires_delta=timedelta(minutes=60) )
            
         
        return {"access_token": access_token, "token_type": "bearer"}
    
   


