from fastapi import APIRouter, Request, UploadFile, File, Depends, Form
from app.controllers import post_controller
from app.middlewares.auth import is_authenticated

router = APIRouter()

@router.post("/addpost")
async def add_post(
    request: Request,
    image: UploadFile = File(...),
    _: Request = Depends(is_authenticated)
):
    return await post_controller.add_new_post(request, image)

@router.get("/all")
async def get_all_posts():
    return await post_controller.get_all_post()

@router.get("/userpost/all")
async def get_user_posts(request: Request = Depends(is_authenticated)):
    return await post_controller.get_user_post(request.state.user_id)

@router.get("/{id}/like")
async def like(id: str, request: Request = Depends(is_authenticated)):
    return await post_controller.like_post(request.state.user_id, id)

@router.get("/{id}/dislike")
async def dislike(id: str, request: Request = Depends(is_authenticated)):
    return await post_controller.dislike_post(request.state.user_id, id)

@router.post("/{id}/comment")
async def comment(id: str, request: Request = Depends(is_authenticated)):
    data = await request.json()
    return await post_controller.add_comment(request.state.user_id, id, data["text"])

@router.post("/{id}/comment/all")
async def get_comments(id: str):
    return await post_controller.get_comments(id)

@router.delete("/delete/{id}")
async def delete(id: str, request: Request = Depends(is_authenticated)):
    return await post_controller.delete_post(request.state.user_id, id)

@router.get("/{id}/bookmark")
async def bookmark(id: str, request: Request = Depends(is_authenticated)):
    return await post_controller.bookmark_post(request.state.user_id, id)

