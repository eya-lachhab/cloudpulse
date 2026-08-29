from fastapi import FastAPI

from app.health import router as health_router
from app.system import router as system_router

app = FastAPI(
    title="CloudPulse",
    description="Cloud-native system monitoring platform",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(system_router)


@app.get("/")
def root():
    return {
        "application": "CloudPulse",
        "version": "0.1.0",
        "status": "running",
    }