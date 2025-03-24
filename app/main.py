from fastapi import FastAPI,HTTPException
from app.routes import user_router 
from pydantic import BaseModel

app = FastAPI()

users = [{"id":1,"name":"manish","email":"manish@gmail.com"},{"id":2,"name":"anish","email":"anish@gmail.com"}]

# Include the user router
app.include_router(user_router, prefix="/users", tags=["Users"])




