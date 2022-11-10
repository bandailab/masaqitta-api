from typing import List
from fastapi import APIRouter, HTTPException
from db.tweet import (
    fetch_all_tweets,
    fetch_one_tweet,
    create_tweet,
    update_tweet,
    remove_tweet
)
from schemas.tweet import Tweet

tweet_router = APIRouter()

@tweet_router.get("/tweets/", response_model=List[Tweet], tags=["tweets"])
async def get_tweet():
  response = await fetch_all_tweets()
  return response

@tweet_router.get("/tweets/{id}", response_model=Tweet, tags=["tweets"])
async def get_tweet_by_id(id):
  response = await fetch_one_tweet(id)
  if response:
    return response
  raise HTTPException(404, f"there is no tweet item with this id {id}")

@tweet_router.post("/tweets/", response_model=Tweet, tags=["tweets"])
async def post_tweet(tweet: Tweet):
  response = await create_tweet(tweet.dict())
  if response:
    return response
    raise HTTPException(400, "Sometheng went wrong / Bad Request", tags=["tweets"])

@tweet_router.put("/tweets/{id}/", response_model=Tweet, tags=["tweets"])
async def put_tweet(id:str, desc:str):
  response = await update_tweet(id, desc)
  if response:
    return response
  raise HTTPException(404, f"there is no tweet item with this id {id}")

@tweet_router.delete("/tweets/{id}", tags=["tweets"])
async def delete_tweet(id):
  response = await remove_tweet(id)
  if response:
    return "Successfully deleted tweet item!"
  raise HTTPException(404, f"there is no tweet item with this id {id}")
