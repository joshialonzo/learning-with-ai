# Tutorial 7 — Infisical Integration

## Goal
- Integrate Infisical for secrets management
- Retrieve secrets and write to config.yaml
- Pass secrets as environment variables to Docker Compose
- Add integration test for secrets

## 7.1 Install Infisical CLI

Follow instructions at https://infisical.com/docs/cli/installation

```bash
curl -sSf https://infisical.com/install.sh | sh
```

## 7.2 Authenticate and Pull Secrets

Authenticate with Infisical:

```bash
infisical login
```

Pull secrets for your project:

```bash
infisical export --env=dev --format=yaml --output=config.yaml
```

## 7.3 Use config.yaml in Docker Compose

Update your Docker Compose file to load environment variables from config.yaml:

```yaml
services:
  web:
    # ...existing code...
    env_file:
      - config.yaml
  db:
    # ...existing code...
  redis:
    # ...existing code...
```

## 7.4 Update FastAPI App to Use Secrets

Read secrets from environment variables in `main.py`:

```python
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/secrets")
def secrets():
    secret_value = os.getenv("MY_SECRET")
    return {"MY_SECRET": secret_value}
```

## 7.5 Integration Test

Create `test_secrets.py`:

```python
import httpx

def test_secrets():
    response = httpx.get("http://localhost:8000/secrets")
    assert response.status_code == 200
    assert "MY_SECRET" in response.json()
```

Run the test:

```bash
uv pip install pytest httpx
pytest test_secrets.py
```

---

## Next Steps
Proceed to Tutorial 8 for end-to-end testing.