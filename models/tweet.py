from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime

from db import Base

from models import Favorite

class Tweet(Base):
    __tablename__ = "tweet"

    tweet_id = Column("tweet_id", Integer, primary_key=True, autoincrement=True, index=True)
    text = Column("text", String(512))
    createdAt = Column("createdat", DATETIME, default=datetime.now, nullable=False)

    favorite = relationship("Favorite", secondary=Favorite, back_populates="tweets")
