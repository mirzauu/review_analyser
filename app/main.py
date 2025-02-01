from fastapi import FastAPI
from .database import engine, Base
from .api import router

app = FastAPI(
    title="FastAPI with Celery",
    description="An API that integrates FastAPI with Celery for asynchronous processing.",
    version="1.0.0",
)


@app.on_event("startup")
def initialize_database():
    """
    Initialize database tables on startup.
    """
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Database initialization failed: {e}")


# Include API router
app.include_router(router)


@app.get("/", tags=["Root"])
def home():
    """
    Root endpoint to check if API is running.
    """
    return {"message": "Welcome to FastAPI with Celery"}
