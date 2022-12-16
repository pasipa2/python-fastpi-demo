# project/app/main.py

import sys

from fastapi import FastAPI, Depends

from app.config import get_settings, Settings


app = FastAPI()

requests_received = int(0)

def requester_counter():
    global requests_received
    requests_received += 1
    return requests_received


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    payload = {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
        "instance_id": settings.id,
        "requests": requester_counter(),
        "server": settings.hostname
    }

    return payload
