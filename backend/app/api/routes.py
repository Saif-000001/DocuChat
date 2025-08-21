from fastapi import APIRouter, HTTPException
from ..models.chat import ChatRequest, ChatResponse
from ..services.chatbot import MedicalChatbot

router = APIRouter()
chatbot = MedicalChatbot()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    return chatbot.get_answer(request.message)

@router.post("/initialize")
async def initialize_documents():
    try:
        chatbot.initialize_vector_store()
        return {"message": "Vector store initialized successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Initialization failed: {str(e)}")
