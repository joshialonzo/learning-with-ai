# Tutorial 1 — uv and Project Configuration

## Goal
- Install Python 3.12
- Install uv
- Initialize project directory
- Create virtual environment and install dependencies
- Set up pyproject.toml for project metadata and dev dependencies

## 1.1 Install Python 3.12

### MacOS
```bash
brew install python@3.12
```

### Linux
Refer to your distribution’s package manager or download from python.org.

## 1.2 Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
# Or via Homebrew
brew install uv

## 1.3 Create Project Directory

```bash
mkdir fastapi-infisical-project
cd fastapi-infisical-project
```

## 1.4 Initialize uv Virtual Environment

```bash
uv venv
```

## 1.5 Install Initial Dependencies

```bash
uv pip install fastapi uvicorn
```

## 1.6 Set Up pyproject.toml

Create a `pyproject.toml` file with project metadata and dev dependencies:

```toml
[project]
name = "fastapi-infisical-project"
version = "0.1.0"
description = "FastAPI project with Infisical, PostgreSQL, and Redis"
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["fastapi", "uvicorn"]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.3",
    "pytest-cov>=4.1.0",
    "httpx>=0.25.1",
    "black>=23.11.0",
    "ruff>=0.1.6",
    "pyright>=1.1.350",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## 1.7 Verify Environment

```bash
uv pip install ".[dev]"
pytest --version
uv --version
```

---

## Next Steps
Proceed to Tutorial 2 to build the FastAPI application.
