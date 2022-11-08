from typing import Union, Optional
from pydantic import BaseModel, Field
import datetime

class Favorite(BaseModel):
    isFavorite: str = Field(None)
    count: int

class TweetBase(BaseModel):
    name: str = Field(None)
    userName: str = Field(None)
    imageURL: str = Field(None)

class TweetCreate(TweetBase):
    pass

class Tweet(TweetBase):
    tweet_id: int
    createdAt: datetime.datetime = Field(None)
    favorite: Union[Favorite, None] = Field(None)

    class Config:
        orm_mode: True

class TweetCreateResponse(TweetBase):
    tweet_id: int
    following: int
    follower: int

    class Config:
        orm_mode: True
