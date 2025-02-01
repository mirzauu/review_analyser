from sqlalchemy.orm import Session
from . import models

def get_latest_reviews(session: Session):
    return session.query(models.ReviewHistory).order_by(models.ReviewHistory.created_at.desc()).limit(5).all()
