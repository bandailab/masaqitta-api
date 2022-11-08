from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime

from db import Base

class Follow(Base):
    __tablename__ = "follow"

    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    tweet_id = Column(Integer, ForeignKey('tweet.tweet_id'), primary_key=True)

    user = relationship("User")
    tweet = relationship("Tweet")
