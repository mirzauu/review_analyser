from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class ReviewHistory(Base):
    __tablename__ = "review_history"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=True)
    stars = Column(Integer, nullable=False)
    review_id = Column(String(255), nullable=False, index=True)
    tone = Column(String(255), nullable=True)
    sentiment = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = relationship("Category", back_populates="reviews")

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    reviews = relationship("ReviewHistory", back_populates="category")

class AccessLog(Base):
    __tablename__ = "access_log"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
