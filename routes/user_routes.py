from fastapi import APIRouter, Request, Depends
from app.controllers import user_controller
from app.middlewares.auth import is_authenticated

router = APIRouter()

@router.post("/register")
async def register(request: Request):
    return await user_controller.register(request)

@router.post("/login")
async def login(request: Request):
    return await user_controller.login(request)

@router.get("/logout")
async def logout():
    return await user_controller.logout()

@router.get("/{id}/profile")
async def get_profile(id: str, _: Request = Depends(is_authenticated)):
    return await user_controller.get_profile(id)

@router.post("/profile/edit")
async def edit_profile(request: Request = Depends(is_authenticated)):
    return await user_controller.edit_profile(request)

@router.get("/suggested")
async def suggested_users(request: Request = Depends(is_authenticated)):
    return await user_controller.get_suggested_users(request.state.user_id)

@router.post("/followorunfollow/{id}")
async def follow(id: str, request: Request = Depends(is_authenticated)):
    return await user_controller.follow_or_unfollow(request, id)

