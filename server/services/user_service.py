from sqlalchemy.orm import Session  
from ..models import user  
from ..schemas import user_schema  
from ..database import get_db  
from fastapi import Depends, HTTPException  
from passlib.context import CryptContext  

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  

def get_password_hash(password):  
    return pwd_context.hash(password)  

def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):  
    db_user = user.User(email=user.email, hashed_password=get_password_hash(user.password), full_name=user.full_name)  
    db.add(db_user)  
    db.commit()  
    db.refresh(db_user)  
    return db_user  

def authenticate_user(user_login: user_schema.UserLogin, db: Session = Depends(get_db)):  
    # Logic to authenticate user  
    pass