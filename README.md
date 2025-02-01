# FastAPI Review Analysis System

## Description
The **FastAPI Review Analysis System** is a web application that processes and analyzes user reviews. It utilizes **FastAPI** for the backend, **Celery** for asynchronous task processing, and **OpenAI's GPT** to analyze the tone and sentiment of reviews. The system supports review categorization, historical logging.

---
## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Celery Tasks](#celery-tasks)
- [Project Structure](#project-structure)


---
## Features
✅ **Review Submission**: Users can submit reviews with star ratings and category selection.  
✅ **Tone & Sentiment Analysis**: AI-powered analysis of review text.  
✅ **Review History**: Stores and retrieves the latest reviews per category.  
✅ **Asynchronous Processing**: Uses Celery workers to handle sentiment analysis and logging.  
✅ **Logging API Access**: Tracks API usage for analytics.  
✅ **Pagination Support**: Fetches reviews efficiently with pagination.

---
## Tech Stack
- **FastAPI** (Backend Framework)
- **SQLAlchemy** (Database ORM)
- **PostgreSQL** (Database)
- **Celery** (Task Queue)
- **Redis** (Message Broker)
- **OpenAI API** (For text analysis)
- **Pydantic** (Schema validation)


---
## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/mirzauu/review_analyser.git

```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
```bash
alembic upgrade head  # Apply database migrations
```

### 5. Start Redis (Required for Celery)
Ensure you have Redis installed and running:
```bash
redis-server
```

### 6. Start the Celery Worker
```bash
celery -A app.celery_worker.celery_app worker --loglevel=info
```

### 7. Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

---
## Environment Variables
Create a `.env` file in the project root and add:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
OPENAI_API_KEY=your_openai_api_key
```

---
## API Endpoints

### **Review Management**
- `POST /reviews/` → Create a new review.
- `GET /reviews/trends?category_id={id}&page={page}` → Fetch paginated reviews.

### **Category Management**
- `POST /categories/` → Create a new category.

### **General**
- `GET /` → Home route.

---
## Celery Tasks
- **log_access(log_text: str)** → Logs API access.
- **update_review_tone_sentiment(review_id: int)** → Processes and updates sentiment analysis.

---
## Project Structure
```
app/
│── ai_utils.py         # OpenAI API integration for sentiment analysis
│── api.py              # FastAPI route handlers
│── celery_worker.py    # Celery worker setup
│── crud.py             # Database queries
│── database.py         # SQLAlchemy database setup
│── main.py             # FastAPI app entry point
│── models.py           # SQLAlchemy models
│── schemas.py          # Pydantic schemas
│── tasks.py            # Celery task definitions
│── .env                # Environment variables (ignored in Git)
│── requirements.txt    # Python dependencies
```

---


🚀 **Developed with FastAPI & Celery** 🚀

