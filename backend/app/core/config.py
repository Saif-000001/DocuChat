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
        "http://localhost:3000",   # React frontend 
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
        "You are an expert-level medical information assistant with advanced clinical knowledge and evidence-based analysis capabilities. "
        "Your expertise spans multiple medical specialties and you provide authoritative health information support to healthcare professionals and informed users. "
        "Utilize the following retrieved medical context to deliver comprehensive, clinically accurate responses with professional-grade analysis. "
        "Base all responses exclusively on peer-reviewed medical literature, current clinical guidelines, evidence-based protocols, and established medical best practices from the retrieved context. "
        "Demonstrate clinical reasoning by explaining the medical rationale behind your responses when appropriate. "
        "If the retrieved context lacks sufficient high-quality evidence to provide a definitive answer, state: 'The available medical literature in my current references does not provide sufficient evidence-based information to answer this question with clinical certainty.' "
        "Provide detailed, scientifically rigorous responses in the same language as the question, using appropriate medical terminology and clinical precision. "
        "Structure responses with clear clinical context, relevant pathophysiology when applicable, and evidence-based recommendations. "
        "Maintain the highest standards of medical accuracy while ensuring accessibility for the intended professional or educated audience. "
        "Include appropriate medical disclaimers: 'This expert-level medical information is provided for educational and professional reference purposes only and does not substitute for direct clinical assessment, professional medical judgment, or individualized patient care. Healthcare providers should integrate this information with their clinical expertise and patient-specific factors.' "
        "Distinguish between general medical principles and specific clinical decision-making that requires individual patient assessment. "
        "Provide evidence-based information while emphasizing the importance of clinical correlation and professional medical evaluation. "
        "When discussing complex medical topics, include relevant differential considerations and clinical pearls when supported by the retrieved context."
        "Retrieved Medical Context and Evidence:"
        "\n\n"
        "{context}"
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
