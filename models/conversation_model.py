# models/conversation_model.py

from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class ConversationModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    participants: List[str]
    messages: List[str] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

