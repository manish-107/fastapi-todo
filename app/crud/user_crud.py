# services/user_service.py
from app.schemas.user_schema import Users as UserSchema
from sqlalchemy.orm import Session
from app.models.models import Users as UserModel
from pydantic import EmailStr
from sqlalchemy import select


class UserService:
    @staticmethod
    def create_user(userData: UserSchema, db: Session):
        db_user = UserModel(**userData.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_userby_email(email:EmailStr,db:Session):
        stmt =  select(UserModel).where(UserModel.email == email)
        result = db.execute(stmt)
        return result.scalars().first()
        # return db.query(UserModel).filter(UserModel.email == email).first() 
