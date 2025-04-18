from fastapi import FastAPI,APIRouter,Depends
from app.schemas.user_schema import Users,SigniRequest
from sqlalchemy.orm import Session
from app.crud.user_crud import UserService
from app.database import get_db
from starlette.responses import JSONResponse

app = FastAPI()

@app.post("/signup")
def signup_user(userData:Users,db:Session = Depends(get_db)):

    userExists = UserService.get_userby_email(userData.email,db)

    if userExists:
        return JSONResponse({"msg" :"User already exists"})

    userDetail = UserService.create_user(userData,db)
    return {"msg":userDetail}

@app.post("/signin")
def signin_user(signindata: SigniRequest, db: Session = Depends(get_db)):
    userExists = UserService.get_userby_email(signindata.email, db)

    if not userExists:
        return JSONResponse(status_code=404, content={"msg": "User doesn't exist"})
    
    if userExists.password != signindata.password:
        return JSONResponse(status_code=401, content={"msg": "Password doesn't match"})
    
    return {"msg": "token"}

@app.get("/")
def get_user():
    return {"msg":"hello"}