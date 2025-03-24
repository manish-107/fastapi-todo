from fastapi import APIRouter, HTTPException
from app.db.database import user_collection
from app.db.models import Users

router = APIRouter()

@router.get("/")
async def get_all_users():
    users = await user_collection.find().to_list(length=None)  
    return users

@router.post("/")
async def addUsers(user: Users):
    user_dict = user.model_dump() 
    result = await user_collection.insert_one(user_dict)
    return {"message": "User added successfully", "id": str(result.inserted_id)}

@router.get("/{email}")
async def get_user_by_email(email: str):
    user = await user_collection.find_one({"email": email}) 
    if user:
        return {"name": user["username"], "email": user["email"]}  

    raise HTTPException(status_code=404, detail="User not found")
