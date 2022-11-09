from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime

from db import Base, Tweet

from models import Favorite

class User(Base):
    __tablename__ = "user"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True, index=True)
    name = Column("name", String(128))
    userName = Column("username", String(32), unique=True)
    imageURL = Column("imageurl", String(256))

    grade = relationship("Grade", back_populate="users")

    favorite = relationship("Favorite", secondary=Favorite, back_populates="users")

    follow = relationship("Follow", secondary=Tweet, back_populate="users")
    follower = relationship("Follow", secondary=Tweet, back_populate="users")
    
