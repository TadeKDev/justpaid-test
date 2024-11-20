from fastapi import FastAPI  
from .routers import auth, search, quotes, reviews, chat  
from .database import engine, Base  
import uvicorn

# Create database tables  
Base.metadata.create_all(bind=engine)  

app = FastAPI()  

# Include routers  
app.include_router(auth.router)  
app.include_router(search.router)  
app.include_router(quotes.router)  
app.include_router(reviews.router)
app.include_router(chat.router) 


if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8000)