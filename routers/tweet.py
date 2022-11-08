from fastapi import APIRouter

router = APIRouter()

# Tweet
@router.get("/tweets", tags=["tweets"])
async def list_tweets():
    pass

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
