from fastapi import Request
from app.utils.db import db

async def send_message(request: Request, receiver_id: str):
    data = await request.json()
    sender_id = request.state.user_id
    message = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "message": data["message"]
    }
    await db["messages"].insert_one(message)
    return {"message": "Message sent"}

async def get_messages(request: Request, user_id: str):
    me = request.state.user_id
    messages = db["messages"].find({
        "$or": [
            {"sender_id": me, "receiver_id": user_id},
            {"sender_id": user_id, "receiver_id": me}
        ]
    })
    return [m async for m in messages]

