from fastapi import APIRouter, Depends  
from ..schemas import user_schema  
from ..services import user_service  

router = APIRouter(prefix="/auth", tags=["auth"])  

@router.post("/register", response_model=user_schema.UserResponse)  
def register(user: user_schema.UserCreate):  
    return user_service.create_user(user)  

@router.post("/login")  
def login(user: user_schema.UserLogin):  
    return user_service.authenticate_user(user)