from fastapi import APIRouter, Request, Depends
from app.controllers import message_controller
from app.middlewares.auth import is_authenticated

router = APIRouter()

@router.post("/send/{id}")
async def send_message(id: str, request: Request = Depends(is_authenticated)):
    return await message_controller.send_message(request, id)

@router.get("/all/{id}")
async def get_all_messages(id: str, request: Request = Depends(is_authenticated)):
    return await message_controller.get_messages(request, id)

