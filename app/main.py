from fastapi import FastAPI
from app.api import user_router 

app = FastAPI()

# Include the user router
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}
