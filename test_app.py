import httpx


def test_root():
    response = httpx.get("http://127.0.0.1:8000/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
