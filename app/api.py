from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import ReviewHistory,Category
from .tasks import log_access, update_review_tone_sentiment
from .schemas import ReviewCreate, ReviewResponse,CategoryCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/reviews/trends")
def get_reviews(
    category_id: int = Query(..., description="Category ID to filter reviews"),
    page: int = Query(1, description="Page number"),
    db: Session = Depends(get_db)
):
    """Fetch all reviews for a category with pagination"""
    
    # Call Celery Task to Log API Access
    log_access.delay(f"GET /reviews/?category_id={category_id}")

    page_size = 15
    offset = (page - 1) * page_size

    # Get latest review for each review_id
    latest_reviews = (
        db.query(ReviewHistory)
        .filter(ReviewHistory.category_id == category_id)
        .order_by(ReviewHistory.created_at.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )


    for review in latest_reviews:
        if review.tone is None or review.sentiment is None:
            update_review_tone_sentiment.delay(review.id)
            task_result = update_review_tone_sentiment.delay(review.id)
            task_result.get()  # Wait until Celery task is completed

    return {"reviews": latest_reviews}



@router.post("/reviews/", response_model=ReviewResponse)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    """Create a new review in the database."""
    
    # Create review entry
    new_review = ReviewHistory(
        text=review.text,
        stars=review.stars,
        review_id=review.review_id,
        category_id=review.category_id
    )
    
    db.add(new_review)
    db.commit()
    db.refresh(new_review)

 
    log_access.delay(f"POST /reviews/ {review.review_id}")

    return new_review


@router.post("/categories/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """Create a new category"""
    new_category = Category(name=category.name, description=category.description)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
