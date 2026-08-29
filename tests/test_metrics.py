from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_metrics_endpoint():
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "cloudpulse_cpu_usage_percent" in response.text
    assert "cloudpulse_memory_usage_percent" in response.text
    assert "cloudpulse_disk_usage_percent" in response.text
    assert "cloudpulse_uptime_seconds" in response.text


def test_http_request_metrics():
    client.get("/health")

    response = client.get("/metrics")

    assert response.status_code == 200
    assert "cloudpulse_http_requests_total" in response.text
    assert 'endpoint="/health"' in response.text
    assert 'method="GET"' in response.text
    assert 'status="200"' in response.text