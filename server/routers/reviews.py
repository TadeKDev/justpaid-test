from fastapi import APIRouter  

router = APIRouter(prefix="/quotes", tags=["quotes"])  

@router.post("/")  
def request_quote():  
    return {"message": "Quote requested"}