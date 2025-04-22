from fastapi import FastAPI,Request,Depends
from app.schemas.user_schema import Users,SigniRequest
from sqlalchemy.orm import Session
from app.crud.user_crud import UserService
from app.database import get_db
from starlette.responses import JSONResponse
from app.services.auth_service import create_access_token
from app.middlewares.auth_middlware import TokenValidatorMiddleware

app = FastAPI()
app.add_middleware(TokenValidatorMiddleware)
#update

@app.post("/signup")
def signup_user(userData:Users,db:Session = Depends(get_db)):

    userExists = UserService.get_userby_email(userData.email,db)

    if userExists:
        return JSONResponse({"msg" :"User already exists"})

    userDetail = UserService.create_user(userData,db)
    return {"msg":userDetail}

@app.post("/signin")
def signin_user(signindata: SigniRequest, db: Session = Depends(get_db)):
    user, role_name = UserService.get_userby_email(signindata.email, db)
    
    if not user:
        return JSONResponse(status_code=404, content={"msg": "User doesn't exist"})
    
    if user.password != signindata.password:
        return JSONResponse(status_code=401, content={"msg": "Password doesn't match"})
    
    access_token = create_access_token(data={"sub": user.email, "role": role_name})
    
    return {"access_token": access_token, "token_type": "bearer","msg":f"Welcome {role_name}" }


@app.get("/getUsers")
def get_users(db: Session = Depends(get_db)):
    users = UserService.get_all_users(db)
    return {"users":users}



@app.get("/dashboard")
def dashboard(request: Request):
    user = request.state.user
    return {"msg": f"Hello {user['email']}, your role is {user['role']}"}

@app.get("/")
def get_user():
    return {"msg":"hello"}