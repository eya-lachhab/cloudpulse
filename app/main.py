import time

from fastapi import FastAPI, Request

from app.health import router as health_router
from app.metrics import (
    http_request_duration,
    http_requests_total,
    router as metrics_router,
)
from app.system import router as system_router

app = FastAPI(
    title="CloudPulse",
    description="Cloud-native system monitoring platform",
    version="0.1.0",
)


@app.middleware("http")
async def record_request_metrics(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    endpoint = request.url.path
    method = request.method
    status = str(response.status_code)

    http_requests_total.labels(
        method=method,
        endpoint=endpoint,
        status=status,
    ).inc()

    http_request_duration.labels(
        method=method,
        endpoint=endpoint,
    ).observe(duration)

    return response


app.include_router(health_router)
app.include_router(system_router)
app.include_router(metrics_router)


@app.get("/")
def root():
    return {
        "application": "CloudPulse",
        "version": "0.1.0",
        "status": "running",
    }