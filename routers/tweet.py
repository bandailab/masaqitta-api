from fastapi import APIRouter

from typing import List
import datetime
import schemas.tweet as tweet_schema

router = APIRouter()

# Tweet
@router.get("/tweets", tags=["tweets"], response_model=List[tweet_schema.Tweet])
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

@router.get("/tweets/{tweet_id}", tags=["tweets"], response_model=tweet_schema.Tweet)
async def get_tweet(tweet_id: int):
    return tweet_schema.Tweet(
        tweet_id=tweet_id, 
        name='Shota Minegishi', 
        userName='@smngs', 
        imageURL="https://yahoo.co.jp",
        createdAt=datetime.datetime.now(),
        favorite={
            "isFavorite": False,
            "count": 30
        }
    )

@router.post("/tweets", tags=["tweets"], response_model=tweet_schema.TweetCreateResponse)
async def create_tweet(tweet_body: tweet_schema.TweetCreate):
    return tweet_schema.TweetCreateResponse(tweet_id=1, **tweet_body.dict())

@router.put("/tweets/{tweet_id}", tags=["tweets"], response_model=tweet_schema.TweetCreateResponse)
async def update_tweet(tweet_body: tweet_schema.TweetCreate):
    return tweet_schema.TweetCreateResponse(tweet_id={tweet_id}, **tweet_body.dict())

@router.delete("/tweets/{tweet_id}", tags=["tweets"], response_model=None)
async def delete_tweet(tweet_id: int):
    return
