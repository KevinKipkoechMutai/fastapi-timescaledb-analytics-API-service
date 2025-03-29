from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import Union


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}