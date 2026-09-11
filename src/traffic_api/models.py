from datetime import datetime
from pydantic import BaseModel


class TrafficEvent(BaseModel):
    sensor_id: str
    road_id: str
    vehicle_count: int
    average_speed: float
    congestion_level: str
    timestamp: datetime
