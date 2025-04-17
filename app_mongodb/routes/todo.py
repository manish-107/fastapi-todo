from fastapi import APIRouter,Depends
from app.middlewares.auth_middlware import auth_middleware

todo_router = APIRouter()

@todo_router.get("/")
async def get_all_todos_or_by_id(id:str = None,payload = Depends(auth_middleware)):
    return {"id":id,"payload" : payload}