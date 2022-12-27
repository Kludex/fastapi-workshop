"""
This is a simple FastAPI application.

You can run it with uvicorn:

    uvicorn main:app

And then visit http://localhost:8000 in your browser.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}
