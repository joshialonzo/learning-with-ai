# Tutorial 2 — FastAPI Application

## Goal
- Create a basic FastAPI app
- Add a root endpoint
- Write integration tests

## 2.1 Create main.py

Create a file named `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## 2.2 Run FastAPI App

```bash
uvicorn main:app --reload
```

## 2.3 Integration Test

Create a file named `test_app.py`:

```python
import httpx

def test_root():
    response = httpx.get("http://127.0.0.1:8000/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

Install test dependencies:

```bash
uv pip install pytest httpx
```

Run the test:

```bash
pytest test_app.py
```

---

## Next Steps
Proceed to Tutorial 3 to dockerize the FastAPI application.
