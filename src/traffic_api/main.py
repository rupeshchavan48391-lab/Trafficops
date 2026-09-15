from fastapi import FastAPI

from src.traffic_api.models import TrafficEvent
from src.traffic_api.rabbitmq import publish_event


app = FastAPI(
    title="TrafficOps API",
    description="Cloud-Native Smart Traffic Management & Incident Response Platform",
    version="1.0.0",
)


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


@app.post("/events")
def create_event(event: TrafficEvent):
    publish_event(event.model_dump(mode="json"))

    return {
        "message": "Traffic event published to RabbitMQ successfully.",
        "event": event,
    }
