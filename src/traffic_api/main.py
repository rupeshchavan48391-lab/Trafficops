from fastapi import FastAPI

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
