from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router as api_router
from .core.config import settings

# Initialize FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,  
    version=settings.VERSION      
)
# Apply CORS middleware (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # List of allowed origins from settings
    allow_credentials=True,                  # Allow cookies and authentication headers
    allow_methods=["*"],                      # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],                      # Allow all custom headers
)
# Register API routes from the routes module
app.include_router(api_router)

# Root endpoint for health check / quick status
@app.get("/")
async def root():
    """
    Basic health check endpoint.
    Useful for verifying that the API is running.
    """
    return {"message": "Medical Chatbot API is running"}
