from fastapi import FastAPI

from src.traffic_api.database import get_connection
from src.traffic_api.models import TrafficEvent


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
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO traffic_events (
                    sensor_id,
                    road_id,
                    vehicle_count,
                    average_speed,
                    congestion_level,
                    timestamp
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, sensor_id, road_id, vehicle_count,
                          average_speed, congestion_level, timestamp
                """,
                (
                    event.sensor_id,
                    event.road_id,
                    event.vehicle_count,
                    event.average_speed,
                    event.congestion_level,
                    event.timestamp,
                ),
            )

            row = cur.fetchone()

    return {
        "message": "Traffic event stored successfully.",
        "event": row,
    }
