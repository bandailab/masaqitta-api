from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime

from db import Base

class Grade(Base):
    __tablename__ = "grade"

    grade_id = Column("tweetid", Integer, primary_key=True, autoincrement=True, index=True)
    grade_name = Column("name", String(128))
    grade_color = Column("name", String(128))

    user = relationship("User", back_populates="grade")
