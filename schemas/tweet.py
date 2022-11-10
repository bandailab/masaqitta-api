from typing import Union
from pydantic import BaseModel

class Like(BaseModel):
    isLike: bool
    count: int

class Retweet(BaseModel):
    isRetweet: bool
    count: int

class Reply(BaseModel):
    isReply: bool
    count: int

class Tweet(BaseModel):
    key: int
    name: str
    userName: str
    imageURL: str
    text: str
    like: Union[Like, None]
    retweet: Union[Retweet, None]
    reply: Union[Reply, None]
