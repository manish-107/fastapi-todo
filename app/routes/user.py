from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import Users
from app.crud.user_crud import UserService
from pydantic import EmailStr

router = APIRouter()

@router.get("/")
async def get_all_users():
    users = await UserService.get_all_users() 
    return users

@router.post("/")
async def addUsers(user: Users):
    result = await UserService.create_user(user)
    return {"message": "User added successfully", "id": str(result.inserted_id)}

@router.get("/{email}")
async def get_user_by_email(email: EmailStr):
    user = await UserService.get_userby_email(email)
    if user:
        return {"name": user["name"], "email": user["email"]}  

    raise HTTPException(status_code=404, detail="User not found")
