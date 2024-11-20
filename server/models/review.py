from sqlalchemy import Column, Integer, String, ForeignKey  
from sqlalchemy.orm import relationship  
from ..database import Base  

class Review(Base):  
    __tablename__ = "reviews"  
    
    id = Column(Integer, primary_key=True, index=True)  
    user_id = Column(Integer, ForeignKey('users.id'))  
    expert_id = Column(Integer, ForeignKey('financial_experts.id'))  
    rating = Column(Integer)  
    comment = Column(String)  

    financial_expert = relationship("FinancialExpert", back_populates="reviews")  
    user = relationship("User", back_populates="reviews")