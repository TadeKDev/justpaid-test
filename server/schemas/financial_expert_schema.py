from pydantic import BaseModel  

class FinancialExpertBase(BaseModel):  
    name: str  
    expertise: str  
    location: str  

class FinancialExpertCreate(FinancialExpertBase):  
    pass  

class FinancialExpertResponse(FinancialExpertBase):  
    id: int  

    class Config:  
        orm_mode = True