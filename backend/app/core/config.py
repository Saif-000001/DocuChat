import os
from dotenv import load_dotenv
from typing import List
load_dotenv()

class Settings:
    # API Settings
    PROJECT_NAME: str = "Medical Chatbot"
    VERSION: str = "1.0.0"
        
    # CORS Settings
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # External APIs
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    
    # Vector Store Settings
    PINECONE_INDEX_NAME: str = "medical-chatbot"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384

    # prompt 
    PROMPT:str = (
            "You are a professional medical information assistant designed to provide evidence-based health information support. "
            "Use the following pieces of retrieved medical context to answer questions accurately and responsibly. "
            "Base all responses strictly on the provided context from peer-reviewed medical literature, clinical guidelines, and established medical protocols. "
            "If the retrieved context doesn't contain sufficient information to answer the question, clearly state 'I don't have enough information in my current medical references to answer this question accurately.' "
            "Provide concise, accurate responses in the same language as the question, using no more than three clear sentences. "
            "Use appropriate medical terminology while remaining accessible to the intended audience. "
            "Always include the disclaimer: 'This information is for educational purposes only and does not constitute medical advice. Please consult with a qualified healthcare provider for personal medical concerns.' "
            "Never provide specific diagnostic conclusions or treatment recommendations. "
            "Avoid speculation beyond the scope of provided medical context."
            "\n\n"
            "Retrieved Medical Context:"
            "\n"
            "{context}"
    )
    # Chat Settings
    CHAT_MODEL: str = "gemini-1.5-flash"
    MAX_CONTEXT_LENGTH: int = 3
    TEMPERATURE: float = 0.0
    
    # File Processing
    PDF_DATA_PATH: str = "data/"
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 20
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
