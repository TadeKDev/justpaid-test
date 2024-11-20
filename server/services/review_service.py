from sqlalchemy.orm import Session  
from ..models import financial_expert  
from ..schemas import financial_expert_schema  
from ..database import get_db  
from fastapi import Depends  

def search_experts(  
    expertise: str = None,  
    location: str = None,  
    db: Session = Depends(get_db)  
):  
    query = db.query(financial_expert.FinancialExpert)  
    if expertise:  
        query = query.filter_by(expertise=expertise)  
    if location:  
        query = query.filter_by(location=location)  
    return query.all()