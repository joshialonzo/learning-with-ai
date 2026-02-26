FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv
RUN uv pip compile pyproject.toml > requirements.txt
RUN uv pip install --system -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]