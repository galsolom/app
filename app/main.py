
from typing import Optional

from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def healthcheck():
    return "Healthy"

tasks = {"msg": "errorz"}

@app.get("/error", status_code=500)
def error_response(response: Response):
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return tasks["msg"]