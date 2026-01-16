# app/scheduler.py
from redbeat import RedBeatSchedulerEntry
from celery.schedules import schedule
from app.celery_app import celery_app

def create_10s_schedule(user_id: str):
    entry_name = f"user:{user_id}:add_random_10s"

    entry = RedBeatSchedulerEntry(
        name=entry_name,
        task="tasks.add_random_numbers",
        schedule=schedule(10.0),  # 10초
        app=celery_app,
        args=[],
        kwargs={},
        enabled=True,
    )

    entry.save()
    return entry_name
