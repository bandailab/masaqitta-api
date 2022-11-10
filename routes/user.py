from typing import List
from fastapi import APIRouter, HTTPException
from db.user import (
    fetch_all_users,
    fetch_one_user,
    create_user,
    update_user,
    remove_user
)
from schemas.user import User

user_router = APIRouter()

@user_router.get("/users", response_model=List[User], tags=["users"])
async def get_user():
  response = await fetch_all_users()
  return response

@user_router.get("/users/{id}", response_model=User, tags=["users"])
async def get_user_by_id(id):
  response = await fetch_one_user(id)
  if response:
    return response
  raise HTTPException(404, f"there is no User item with this id {id}")

@user_router.post("/users", response_model=User, tags=["users"])
async def post_user(user:User):
  response = await create_user(user.dict())
  if response:
    return response
  raise HTTPException(400, "Sometheng went wrong / Bad Request")

@user_router.put("/users/{id}/", response_model=User, tags=["users"])
async def put_user(id:str, desc:str):
  response = await update_user(id, desc)
  if response:
    return response
  raise HTTPException(404, f"there is no User item with this id {id}")

@user_router.delete("/users/{id}", tags=["users"])
async def delete_user(id):
  response = await remove_user(id)
  if response:
    return "Successfully deleted user item!"
  raise HTTPException(404, f"there is no User item with this id {id}")
