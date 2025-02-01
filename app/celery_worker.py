import os
from celery import Celery


REDIS_BROKER_URL = os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0")
REDIS_BACKEND_URL = os.getenv("REDIS_BACKEND_URL", "redis://localhost:6379/0")


celery_app = Celery("worker", include=["app.tasks"])


celery_app.conf.update(
    broker_url=REDIS_BROKER_URL,
    result_backend=REDIS_BACKEND_URL,
    task_routes={"app.tasks.*": {"queue": "celery"}}
)


if __name__ == "__main__":
    celery_app.start()