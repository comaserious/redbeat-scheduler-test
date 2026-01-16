# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.scheduler import create_10s_schedule

app = FastAPI()

class ScheduleRequest(BaseModel):
    user_id: str

@app.post("/schedule/10-seconds")
def request_schedule(req: ScheduleRequest):
    schedule_name = create_10s_schedule(req.user_id)
    return {
        "message": "10초 스케줄이 등록되었습니다.",
        "schedule_name": schedule_name,
    }
