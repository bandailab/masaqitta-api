from fastapi import APIRouter

from typing import List
import datetime
import schemas.tweet as tweet_schema

router = APIRouter()

# Tweet
@router.get("/tweets", tags=["tweets"])
async def list_tweets():
    return [
        tweet_schema.Tweet(
            tweet_id=1, 
            name='Shota Minegishi', 
            userName='@smngs', 
            imageURL="https://yahoo.co.jp",
            createdAt=datetime.datetime.now(),
            favorite={
                "isFavorite": False,
                "count": 30
            }
        )]

@router.get("/tweets/{tweet_id}", tags=["tweets"])
async def get_tweet():
    pass

@router.post("/tweets", tags=["tweets"])
async def create_tweet():
    pass

@router.put("/tweets/{tweet_id}", tags=["tweets"])
async def update_tweet():
    pass

@router.delete("/tweets/{tweet_id}", tags=["tweets"])
async def delete_tweet():
    pass
