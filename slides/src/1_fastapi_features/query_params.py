"""
This example shows how to use query parameters in FastAPI.

Run the example with:

    uvicorn query_params:app --reload

And then go to http://localhost:8000/?query=myquery
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home(query: str):
    return {"query": query}
