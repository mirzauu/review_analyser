from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CategoryCreate(BaseModel):
    name: str
    description: str

class ReviewCreate(BaseModel):
    text: str
    stars: int
    review_id: str
    category_id: int

class ReviewResponse(BaseModel):
    id: int
    text: str
    stars: int
    review_id: str
    created_at: datetime
    tone: Optional[str] = None
    sentiment: Optional[str] = None
    category_id: int
