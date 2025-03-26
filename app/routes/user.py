from fastapi import APIRouter,Depends,HTTPException
from app.schemas.user_schema import Users
from app.crud.user_crud import UserService
from pydantic import EmailStr
from app.middlewares.auth_middlware import auth_middleware

router = APIRouter()

@router.get("/")
async def get_all_users(payload: dict = Depends(auth_middleware)):
    users = await UserService.get_all_users() 
    return {"users":users,"payload" : payload}

@router.get("/{email}")
async def get_user_by_email(email: EmailStr,payload: dict = Depends(auth_middleware)):
    user = await UserService.get_userby_email(email)
    if user:
        return {"name": user["name"], "email": user["email"],"payload":payload}  

    raise HTTPException(status_code=404, detail="User not found")
