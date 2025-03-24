from fastapi import FastAPI,HTTPException
from app.routes import user_router 
from pydantic import BaseModel

app = FastAPI()

# Include the user router
app.include_router(user_router, prefix="/users", tags=["Users"])




