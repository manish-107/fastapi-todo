from fastapi import FastAPI
from app.api.routes import user_router

app = FastAPI(title="FastApi todo app")

app.include_router(user_router,prefix="/users",tags=["Users"])

@app.get("/")
def read_root():
    return {"message":"hello from Api"}
