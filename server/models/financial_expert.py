from sqlalchemy import Column, Integer, String  
from sqlalchemy.orm import relationship  
from ..database import Base  

class FinancialExpert(Base):  
    __tablename__ = "financial_experts"  
    
    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, index=True)  
    expertise = Column(String)  
    location = Column(String)  

    reviews = relationship("Review", back_populates="financial_expert")