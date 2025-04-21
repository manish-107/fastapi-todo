# services/user_service.py
from app.schemas.user_schema import Users as UserSchema
from sqlalchemy.orm import Session
from app.models.models import Users as UserModel
from app.models.models import Roles as RolesModel
from pydantic import EmailStr
from sqlalchemy import select

class UserService:
    @staticmethod
    def create_user(userData: UserSchema, db: Session):
        try:
            db_user = UserModel(
                username=userData.username,
                email=userData.email,
                password=userData.password
            )
            db.add(db_user)
            db.flush() 

            db_role = RolesModel(
                user_id=db_user.user_id,
                role_name=userData.role
            )
            db.add(db_role)
            db.commit()    
            db.refresh(db_user)
            return {db_user,db_role}

        except Exception as e:
            db.rollback()   
            raise e       

    @staticmethod
    def get_userby_email(email: EmailStr, db: Session):
        stmt = (
            select(UserModel, RolesModel.role_name)
            .join(RolesModel, UserModel.user_id == RolesModel.user_id)
            .where(UserModel.email == email)
        )
        result = db.execute(stmt).first()
        return result
        # return db.query(UserModel).filter(UserModel.email == email).first() 

    @staticmethod
    def get_all_users(db:Session):
        
        stmt = select(
            UserModel.email,
            UserModel.username,
            UserModel.user_id,
            RolesModel.role_name
        ).join(RolesModel,UserModel.user_id == RolesModel.user_id)

        results = db.execute(stmt).all()

        users_with_roles = [
            {
                "user_id": row.user_id,
                "username": row.username,
                "email": row.email,
                "role": row.role_name
            }
            for row in results
        ]

        return users_with_roles
