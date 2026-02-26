# Tutorial 7 — Redis Integration

## Goal
- Add Redis service to Docker Compose
- Connect FastAPI app to Redis
- Add integration test for cache connectivity

## 7.1 Update docker-compose.yml

Add Redis service:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
    env_file:
      - local.env
  db:
    image: postgres:15
    env_file:
      - local.env
    ports:
      - "5432:5432"
  redis:
    image: redis:7
    env_file:
      - local.env
    ports:
      - "6379:6379"
```

## 7.2 Install redis-py

```bash
uv pip install redis
```

## 7.3 Update FastAPI App for Redis

Update `main.py`:

```python
import os
import redis
from fastapi import FastAPI

app = FastAPI()

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(redis_url)

@app.get("/cache-status")
def cache_status():
    try:
        redis_client.set("test", "ok")
        value = redis_client.get("test")
        return {"cache": value.decode()}
    except Exception as e:
        return {"cache": "error", "detail": str(e)}
```

## 7.4 Integration Test

Create `test_cache.py`:

```python
import httpx

def test_cache_status():
    response = httpx.get("http://localhost:8000/cache-status")
    assert response.status_code == 200
    assert response.json()["cache"] == "ok"
```

Run the test:

```bash
uv pip install pytest httpx
pytest test_cache.py
```

---

## Next Steps
Proceed to Tutorial 7 to add Infisical integration.
