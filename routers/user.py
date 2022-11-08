from fastapi import APIRouter

from typing import List
import datetime
import schemas.user as user_schema

router = APIRouter()

# User
@router.get("/users", tags=["users"], response_model=List[user_schema.User])
async def list_users():
    return [user_schema.User(
        user_id=1,
        name="Shota Minegishi",
        userName="@smngs",
        greeting="よろしくお願いします．",
        imageURL="https://bit.ly/dan-abramov",
        following=20,
        follower=30
    )]

@router.get("/users/{user_id}", tags=["users"], response_model=user_schema.User)
async def get_user():
    return user_schema.User(
        user_id=1,
        name="Shota Minegishi",
        userName="@smngs",
        greeting="よろしくお願いします．",
        imageURL="https://bit.ly/dan-abramov",
        following=20,
        follower=30
    )

@router.post("/users", tags=["users"], response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(user_id=1, **user_body.dict())

@router.put("/users/{user_id}", tags=["users"], response_model=user_schema.UserCreateResponse)
async def update_user(user_id: int, user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(user_id=user_id, **user_body.dict())

@router.delete("/users/{user_id}", tags=["users"])
async def delete_user(user_id: int):
    pass
