# Tutorial 8 — End-to-End Testing

## Goal
- Add end-to-end tests for all integrations

## 8.1 Create test_e2e.py

```python
import httpx

def test_e2e():
    # Test root
    r = httpx.get("http://localhost:8000/")
    assert r.status_code == 200
    assert r.json() == {"Hello": "World"}

    # Test DB
    r = httpx.get("http://localhost:8000/db-status")
    assert r.status_code == 200
    assert r.json()["db"] == "connected"

    # Test Redis
    r = httpx.get("http://localhost:8000/cache-status")
    assert r.status_code == 200
    assert r.json()["cache"] == "ok"

    # Test Secrets
    r = httpx.get("http://localhost:8000/secrets")
    assert r.status_code == 200
    assert "MY_SECRET" in r.json()
```

## 8.2 Run the Test

```bash
uv pip install pytest httpx
pytest test_e2e.py
```

---

## Final Notes
You now have a fully integrated FastAPI project with uv, Docker, Docker Compose, PostgreSQL, Redis, Infisical, and end-to-end tests. Adapt these tutorials for your own workflows and extend as needed!
