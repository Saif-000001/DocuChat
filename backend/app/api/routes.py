from fastapi import APIRouter, HTTPException
from ..models.chat import ChatRequest, ChatResponse
from ..services.chatbot import MedicalChatbot

# Create a router instance for grouping chat-related endpoints
router = APIRouter()
# Initialize the chatbot service (singleton instance for reuse across requests)
chatbot = MedicalChatbot()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint:
    - Accepts a user query (ChatRequest).
    - Returns chatbot response with answer and sources.
    """
    if not request.message.strip():
        # Raise HTTP 400 if message is empty or only whitespace
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    # Pass the message to chatbot service and return structured response
    return chatbot.get_answer(request.message)

@router.post("/initialize")
async def initialize_documents():
    """
    Initialization endpoint:
    - Loads, preprocesses, and inserts documents into Pinecone vector database.
    - Useful for first-time setup or refreshing the knowledge base.
    """
    try:
        # Initialize the vector database with processed documents
        chatbot.initialize_vector_store()
        return {"message": "Vector store initialized successfully"}
    except Exception as e:
        # Handle initialization errors gracefully
        raise HTTPException(status_code=500, detail=f"Initialization failed: {str(e)}")
