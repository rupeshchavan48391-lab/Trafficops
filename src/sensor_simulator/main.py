import random
import time

import requests


API_URL = "http://127.0.0.1:8000/events"

SENSORS = [
    {
        "sensor_id": "SENSOR-001",
        "road_id": "NH48-MUM-01",
    },
    {
        "sensor_id": "SENSOR-002",
        "road_id": "NH48-MUM-02",
    },
    {
        "sensor_id": "SENSOR-003",
        "road_id": "NH48-MUM-03",
    },
]


def generate_event():
    sensor = random.choice(SENSORS)

    vehicle_count = random.randint(20, 180)
    average_speed = round(random.uniform(10, 60), 2)

    if average_speed < 20:
        congestion_level = "CRITICAL"
    elif average_speed < 30:
        congestion_level = "HIGH"
    elif average_speed < 45:
        congestion_level = "MEDIUM"
    else:
        congestion_level = "LOW"

    return {
        "sensor_id": sensor["sensor_id"],
        "road_id": sensor["road_id"],
        "vehicle_count": vehicle_count,
        "average_speed": average_speed,
        "congestion_level": congestion_level,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }


def send_event(event):
    response = requests.post(API_URL, json=event)

    print("Sent event:")
    print(event)

    print("API status:", response.status_code)
    print("API response:", response.json())

if __name__ == "__main__":
    while True:
        event = generate_event()
        send_event(event)

        time.sleep(5)
