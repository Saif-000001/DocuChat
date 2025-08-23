import os
from dotenv import load_dotenv
from typing import List

# Load environment variables from .env file 
load_dotenv()

class Settings: 
    # Project Info
    PROJECT_NAME: str = "Medical Chatbot"
    VERSION: str = "1.0.0"
        
    # CORS (Cross-Origin Resource Sharing)
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",   # React + Vite
        "http://localhost:3000",   # React CRA
        "http://localhost:8000"    # FastAPI docs
    ]
    
    # External API Keys (loaded from .env)
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    
    # Vector Store Configuration
    PINECONE_INDEX_NAME: str = "medical-chatbot"  # Name of Pinecone index
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"  # Embedding model
    EMBEDDING_DIMENSION: int = 384  # Dimensionality of chosen embedding model

    # Prompt Engineering
    PROMPT: str = (
        "You are a medical expert assistant providing evidence-based healthcare information. "
        "Answer in 5 sentences or less using the retrieved medical context. "
        "Base responses on peer-reviewed literature and clinical guidelines only. "
        "If context lacks sufficient evidence, state: 'Insufficient evidence-based information available.' "
        "Include disclaimer: 'Educational purposes only - consult healthcare professionals for medical decisions.' "
        "Include necessary emojis as user understand their situation, respond with relevant medical context emojis. "
        "Retrieved Medical Context: {context}"
    )
    # Chat Model Configuration
    CHAT_MODEL: str = "gemini-1.5-flash"  # LLM to use
    MAX_CONTEXT_LENGTH: int = 3  # Number of turns to retain in chat memory
    TEMPERATURE: float = 0.0 

    # Document Processing
    PDF_DATA_PATH: str = "data/"  # Folder to store uploaded PDFs
    CHUNK_SIZE: int = 500         # Text chunk size for splitting documents
    CHUNK_OVERLAP: int = 20       # Overlap between chunks for context continuity
    
    class Config:
        """
        Pydantic Config:
        - Automatically loads values from `.env`
        - Case sensitivity enabled
        """
        env_file = ".env"
        case_sensitive = True
        
# Global settings instance
settings = Settings()
