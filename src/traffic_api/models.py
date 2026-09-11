from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class CongestionLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class TrafficEvent(BaseModel):
    sensor_id: str
    road_id: str
    vehicle_count: int
    average_speed: float
    congestion_level: CongestionLevel
    timestamp: datetime
