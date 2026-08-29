import os
import time

import psutil
from fastapi import APIRouter

router = APIRouter()

BOOT_TIME = psutil.boot_time()


@router.get("/system")
def get_system_info():
    return {
        "hostname": os.uname().nodename if hasattr(os, "uname") else os.environ.get("COMPUTERNAME"),
        "cpu": {
            "usage_percent": psutil.cpu_percent(interval=0.5),
            "cores": psutil.cpu_count(logical=True),
        },
        "memory": {
            "usage_percent": psutil.virtual_memory().percent,
            "total_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        },
        "disk": {
            "usage_percent": psutil.disk_usage("/").percent,
        },
        "uptime_seconds": round(time.time() - BOOT_TIME),
    }