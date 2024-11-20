from pydantic import BaseModel  

class ReviewBase(BaseModel):  
    rating: int  
    comment: str  

class ReviewCreate(ReviewBase):  
    user_id: int  
    expert_id: int  

class ReviewResponse(ReviewBase):  
    id: int  
    user_id: int  
    expert_id: int  

    class Config:  
        orm_mode = True