import httpx


def test_db_status():
    response = httpx.get("http://localhost:8000/db-status")
    assert response.status_code == 200
    assert response.json()["db"] == "connected"
