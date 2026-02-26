# Tutorial 6 — PostgreSQL Integration with local.env

## Goal
- Add PostgreSQL service to Docker Compose
- Use local.env for environment variables
- Connect FastAPI app to PostgreSQL
- Add integration test for DB connectivity

## 6.1 Create local.env

Create a file named `local.env`:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

## 6.2 Update docker-compose.yml

Reference `local.env` in Compose:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    env_file:
      - local.env
  db:
    image: postgres:15
    env_file:
      - local.env
    ports:
      - "5432:5432"
```

## 6.3 Install psycopg2-binary

```bash
uv pip install psycopg2-binary
```

## 6.4 Update FastAPI App for DB

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

## 6.5 Integration Test

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
Proceed to Tutorial 7 to add Redis integration.
