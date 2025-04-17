from fastapi import FastAPI,APIRouter
from schemas.user_schema import Users

app = FastAPI()



@app.post("/signup")
def signup_user(user:Users):

    return {"msg":user}



@app.get("/")
def get_user():
    return {"msg":"hello"}