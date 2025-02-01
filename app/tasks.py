from .celery_worker import celery_app
from .database import SessionLocal
from .models import AccessLog,ReviewHistory
from .ai_utils import analyze_review_tone_sentiment

@celery_app.task
def log_access(log_text: str):
    """Celery Task: Log API calls asynchronously"""
    db = SessionLocal()
    new_log = AccessLog(text=log_text)
    db.add(new_log)
    db.commit()
    db.close()


@celery_app.task
def update_review_tone_sentiment(review_id: int):
    """Celery Task to update tone & sentiment for a review"""
    db = SessionLocal()
    review = db.query(ReviewHistory).filter(ReviewHistory.id == review_id).first()

    if review and (review.tone is None or review.sentiment is None):
        tone, sentiment = analyze_review_tone_sentiment(review.text, review.stars)
        review.tone = tone
        review.sentiment = sentiment
        db.commit()

    db.close()
