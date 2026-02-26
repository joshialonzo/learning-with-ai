import os

import psycopg2
import redis
from fastapi import FastAPI


app = FastAPI()

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(redis_url)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/db-status")
def db_status():
    db_url = os.getenv("DATABASE_URL")
    try:
        conn = psycopg2.connect(db_url)
        conn.close()
        return {"db": "connected"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}


@app.get("/cache-status")
def cache_status():
    try:
        redis_client.set("test", "ok")
        value = redis_client.get("test")
        return {"cache": value.decode()}
    except Exception as e:
        return {"cache": "error", "detail": str(e)}
