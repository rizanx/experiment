from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/echo")
def echo(q: str = "hello"):
    return {"echo": q}
