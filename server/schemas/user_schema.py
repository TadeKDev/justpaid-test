from pydantic import BaseModel  

class UserBase(BaseModel):  
    email: str  
    full_name: str  

class UserCreate(UserBase):  
    password: str  

class UserLogin(BaseModel):  
    email: str  
    password: str  

class UserResponse(UserBase):  
    id: int  

    class Config:  
        orm_mode = True