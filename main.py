# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_route import user_router
from routes.post_route import post_router
from routes.message_route import message_router
from utils.db import connect_db
from socket.socket import socket_manager

import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("URL", "*")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/v1/user")
app.include_router(post_router, prefix="/api/v1/post")
app.include_router(message_router, prefix="/api/v1/message")

connect_db()

@app.get("/")
def read_root():
    return {"message": "API is up and running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 3000)), reload=True)

