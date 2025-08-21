from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router as api_router

app = FastAPI(title="Medical Chatbot API", version="1.0.0")

# Apply middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Medical Chatbot API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
