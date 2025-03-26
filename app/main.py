from fastapi import FastAPI,Request,HTTPException
from app.routes import user_router 
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
# from app.middlewares.auth_middlware import AuthMiddleware
from app.schemas.user_schema import Users,SigniRequest
from app.crud.user_crud import UserService

app = FastAPI()

@app.post("/signin")
async def signin_user(user:SigniRequest):
    result = await UserService.signin_user(user)
    return {"message": "User exists", "id": result}

@app.post("/signup")
async def signup_user(user:Users):
    result = await UserService.create_user(user)
    return {"message": "User added successfully", "id": str(result.inserted_id)}

app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def root_route():
    return {"msg":"hello"}