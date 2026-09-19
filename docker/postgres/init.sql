CREATE TABLE IF NOT EXISTS traffic_events (
    id SERIAL PRIMARY KEY,
    sensor_id VARCHAR(50) NOT NULL,
    road_id VARCHAR(100) NOT NULL,
    vehicle_count INTEGER NOT NULL,
    average_speed DOUBLE PRECISION NOT NULL,
    congestion_level VARCHAR(20) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL
);
