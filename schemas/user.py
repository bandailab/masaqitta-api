from typing import Union, Optional
from pydantic import BaseModel, Field
import datetime

class UserBase(BaseModel):
    name: str = Field(None)
    userName: str = Field(None)
    imageURL: str = Field(None)
    greeting: str = Field(None)

class UserCreate(UserBase):
    password: str = Field(None)

class User(UserBase):
    user_id: int
    following: int
    follower: int

    class Config:
        orm_mode: True

class UserCreateResponse(UserBase):
    user_id: int

    class Config:
        orm_mode: True
