from fastapi import APIRouter, HTTPException  
import requests  

router = APIRouter(prefix="/chat", tags=["chat"])  

@router.post("/")  
def chat_with_bot(user_message: str):  
    # URL to Rasa's REST API endpoint  
    RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"  
    
    if not user_message:  
        raise HTTPException(status_code=400, detail="Message content is required")  

    # Prepare payload for Rasa  
    payload = {"sender": "user", "message": user_message}  

    try:  
        response = requests.post(RASA_SERVER_URL, json=payload)  
        response.raise_for_status()  # Raise an exception for HTTP errors  
        
        messages = response.json()  
        # Extract bot's text response  
        bot_responses = [message["text"] for message in messages if "text" in message]  
        
        return {"responses": bot_responses}  

    except requests.exceptions.RequestException as e:  
        raise HTTPException(status_code=500, detail="Error communicating with the chatbot server")  

# Add this router to the main FastAPI application in main.py  
# app.include_router(chat.router)