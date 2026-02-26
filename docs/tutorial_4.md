# Tutorial 4 — Docker Compose

## Goal
- Use Docker Compose to orchestrate FastAPI app
- Prepare for adding database and cache services

## 4.1 Create docker-compose.yml

Create a `docker-compose.yml` file:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
```

## 4.2 Run with Docker Compose

```bash
docker compose up --build
```

## 4.3 Verify

Visit http://localhost:8000/ or use curl:

```bash
curl http://localhost:8000/
```

---

## Next Steps
Proceed to Tutorial 5 to add PostgreSQL integration.
