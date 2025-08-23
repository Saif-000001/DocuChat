from pydantic import BaseModel
from typing import List, Optional

# For input message 
class ChatRequest(BaseModel):
    message: str

# For output message
class ChatResponse(BaseModel):
    answer: str
    # source_documents: Optional[List[str]] = None
