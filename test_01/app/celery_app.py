# app/celery_app.py
from celery import Celery

celery_app = Celery(
    "demo",
    broker="redis://redis:6379/1",
    backend="redis://redis:6379/1",
    include=['app.tasks']
)

celery_app.conf.update(
    timezone="Asia/Seoul",
    enable_utc=False,

    beat_scheduler="redbeat.RedBeatScheduler",
    redbeat_redis_url="redis://redis:6379/2",
)