from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_system_endpoint():
    response = client.get("/system")

    assert response.status_code == 200

    data = response.json()

    assert "hostname" in data
    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data
    assert "uptime_seconds" in data


def test_system_cpu():
    response = client.get("/system")
    data = response.json()

    assert 0 <= data["cpu"]["usage_percent"] <= 100
    assert data["cpu"]["cores"] > 0


def test_system_memory():
    response = client.get("/system")
    data = response.json()

    assert 0 <= data["memory"]["usage_percent"] <= 100
    assert data["memory"]["total_gb"] > 0


def test_system_disk():
    response = client.get("/system")
    data = response.json()

    assert 0 <= data["disk"]["usage_percent"] <= 100