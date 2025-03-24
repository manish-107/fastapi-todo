from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router = APIRouter()

users = [{"id":1,"name":"manish","email":"manish@gmail.com"},{"id":2,"name":"anish","email":"anish@gmail.com"}]

# Include the user router
# app.include_router(user_router, prefix="/users", tags=["Users"])

class Users(BaseModel):
    id:int
    name:str
    email:str

@router.get("/")
def get_all_users():
     return users

@router.post("/")
def addUsers(user:Users):
    users.append(user)
    return f"User add successfully"

@router.get("/{id}")
def get_user_id(id: int):
    for user in users:
        if(user["id"] == id):
            return f"{user["name"]} and  {user["id"]}"
        else:
            return HTTPException(status_code=404,detail=f"{id} dont exists")
