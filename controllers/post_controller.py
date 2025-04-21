from fastapi import Request, UploadFile, HTTPException
from app.utils.db import db
from app.utils.cloudinary import cloudinary
from app.utils.datauri import get_data_uri
from bson import ObjectId

async def add_new_post(request: Request, image: UploadFile):
    user_id = request.state.user_id
    form = await request.form()
    caption = form.get("caption", "")
    data_uri = get_data_uri(image.file)
    upload_result = cloudinary.uploader.upload(data_uri)
    
    post = {
        "caption": caption,
        "image": upload_result["secure_url"],
        "author": user_id,
        "likes": [],
        "comments": []
    }
    result = await db["posts"].insert_one(post)
    await db["users"].update_one({"_id": user_id}, {"$push": {"posts": str(result.inserted_id)}})
    return {"message": "Post created"}

async def get_all_post():
    posts = db["posts"].find({})
    return [p async for p in posts]

async def get_user_post(user_id: str):
    posts = db["posts"].find({"author": user_id})
    return [p async for p in posts]

async def like_post(user_id: str, post_id: str):
    await db["posts"].update_one({"_id": post_id}, {"$addToSet": {"likes": user_id}})
    return {"message": "Post liked"}

async def dislike_post(user_id: str, post_id: str):
    await db["posts"].update_one({"_id": post_id}, {"$pull": {"likes": user_id}})
    return {"message": "Post disliked"}

async def add_comment(user_id: str, post_id: str, text: str):
    comment = {"author": user_id, "text": text, "post": post_id}
    result = await db["comments"].insert_one(comment)
    await db["posts"].update_one({"_id": post_id}, {"$push": {"comments": str(result.inserted_id)}})
    return {"message": "Comment added"}

async def get_comments(post_id: str):
    comments = db["comments"].find({"post": post_id})
    return [c async for c in comments]

async def delete_post(user_id: str, post_id: str):
    post = await db["posts"].find_one({"_id": post_id})
    if not post or post["author"] != user_id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    await db["posts"].delete_one({"_id": post_id})
    return {"message": "Post deleted"}

async def bookmark_post(user_id: str, post_id: str):
    await db["users"].update_one({"_id": user_id}, {"$addToSet": {"bookmarks": post_id}})
    return {"message": "Post bookmarked"}

