from fastapi import APIRouter, Depends  
from ..schemas import financial_expert_schema  
from ..services import expert_service  

router = APIRouter(prefix="/search", tags=["search"])  

@router.get("/", response_model=list[financial_expert_schema.FinancialExpertResponse])  
def search_experts(  
    expertise: str = None,  
    location: str = None  
):  
    return expert_service.search_experts(expertise, location)