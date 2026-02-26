# Tutorial 5 — PostgreSQL Integration

## Goal
- Add PostgreSQL service to Docker Compose
- Connect FastAPI app to PostgreSQL
- Add integration test for DB connectivity

## 5.1 Update docker-compose.yml

Add PostgreSQL service:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
    ports:
      - "5432:5432"
```

## 5.2 Install psycopg2-binary

```bash
uv pip install psycopg2-binary
```

## 5.3 Update FastAPI App for DB

Update `main.py`:

```python
import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

@app.get("/db-status")
def db_status():
    db_url = os.getenv("DATABASE_URL")
    try:
        conn = psycopg2.connect(db_url)
        conn.close()
        return {"db": "connected"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}
```

## 5.4 Integration Test

Create `test_db.py`:

```python
import httpx

def test_db_status():
    response = httpx.get("http://localhost:8000/db-status")
    assert response.status_code == 200
    assert response.json()["db"] == "connected"
```

Run the test:

```bash
uv pip install pytest httpx
pytest test_db.py
```

---

## Next Steps
Proceed to Tutorial 6 to add Redis integration.
