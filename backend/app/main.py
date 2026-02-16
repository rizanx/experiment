from fastapi import FastAPI

# Simple FastAPI backend for experiment
app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/echo")
def echo(q: str = "hello"):
    return {"echo": q}
