# models/user_model.py

from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from bson import ObjectId

class UserModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    username: str
    email: EmailStr
    password: str
    profile_picture: Optional[str] = ""
    bio: Optional[str] = ""
    gender: Optional[str] = None
    followers: List[str] = []
    following: List[str] = []
    posts: List[str] = []
    bookmarks: List[str] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


