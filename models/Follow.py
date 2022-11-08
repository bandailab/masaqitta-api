from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime

from db import Base

class Follow(Base):
    __tablename__ = "follow"

    follow_from_user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    follow_to_user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)

    follow_from = relationship("User")
    follow_to = relationship("User")
