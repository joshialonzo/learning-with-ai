import httpx


def test_cache_status():
    response = httpx.get("http://localhost:8000/cache-status")
    assert response.status_code == 200
    assert response.json()["cache"] == "ok"
