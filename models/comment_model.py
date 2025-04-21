# models/comment_model.py

from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class CommentModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    text: str
    author: str
    post: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

