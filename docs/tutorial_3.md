# Tutorial 3 — Dockerization

## Goal
- Create a Dockerfile for FastAPI app
- Build and run the app in a container

## 3.1 Create Dockerfile

Create a `Dockerfile` in your project root:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 3.2 Build Docker Image

```bash
export DOCKER_BUILDKIT=1
docker build -t fastapi-infisical-project .
```

## 3.3 Run Docker Container

```bash
docker run -p 8000:8000 fastapi-infisical-project
```

## 3.4 Verify

Visit http://localhost:8000/ in your browser or use curl:

```bash
curl http://localhost:8000/
```

---

## Next Steps
Proceed to Tutorial 4 to add Docker Compose for multi-service orchestration.
