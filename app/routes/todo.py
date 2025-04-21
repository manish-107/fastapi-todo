from fastapi import APIRouter
from app.schemas.user_schema import TodoResponse

todoRouter = APIRouter()

@todoRouter.post("/todo")
def add_todo(todo:TodoResponse):
    pass