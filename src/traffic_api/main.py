from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from src.traffic_api.models import TrafficEvent
from src.traffic_api.rabbitmq import publish_event


app = FastAPI(
    title="TrafficOps API",
    description="Cloud-Native Smart Traffic Management & Incident Response Platform",
    version="1.0.0",
)


BASE_DIR = Path(__file__).resolve().parent
DASHBOARD_FILE = BASE_DIR / "static" / "index.html"


@app.get("/")
def root():
    return {
        "message": "TrafficOps API is running",
        "status": "healthy",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "traffic-api",
    }


@app.get("/dashboard")
def dashboard():
    return FileResponse(DASHBOARD_FILE)


@app.post("/events")
def create_event(event: TrafficEvent):
    publish_event(event.model_dump(mode="json"))

    return {
        "message": "Traffic event published to RabbitMQ successfully.",
        "event": event,
    }
