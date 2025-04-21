# models/post_model.py

from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class PostModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    caption: Optional[str] = ""
    image: str
    author: str
    likes: List[str] = []
    comments: List[str] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

