import time

import psutil
from fastapi import APIRouter, Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Gauge,
    Histogram,
    generate_latest,
)

router = APIRouter()

# System metrics
cpu_usage = Gauge(
    "cloudpulse_cpu_usage_percent",
    "Current CPU usage percentage",
)

memory_usage = Gauge(
    "cloudpulse_memory_usage_percent",
    "Current memory usage percentage",
)

disk_usage = Gauge(
    "cloudpulse_disk_usage_percent",
    "Current disk usage percentage",
)

uptime = Gauge(
    "cloudpulse_uptime_seconds",
    "System uptime in seconds",
)

# HTTP metrics
http_requests_total = Counter(
    "cloudpulse_http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"],
)

http_request_duration = Histogram(
    "cloudpulse_http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
)


def update_system_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=None))
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage("/").percent)
    uptime.set(time.time() - psutil.boot_time())


@router.get("/metrics")
def metrics():
    update_system_metrics()

    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )