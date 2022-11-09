from sqlalchemy.ext.asyncio import AsyncSession

import models.tweet as tweet_model 
import schemas.tweet as tweet_schema


async def create_task(db: AsyncSession, tweet_create: tweet_schema.TweetCreate) -> tweet_model.Tweet:
    tweet = tweet_model.Tweet(**tweet_create.dict())
    db.add(tweet)
    await db.commit()
    await db.refresh(tweet)
    return tweet
