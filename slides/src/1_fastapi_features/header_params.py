"""
This example shows how to use query parameters in FastAPI.

Run the example with:

    uvicorn query_params:app --reload

And then go to http://localhost:8000/?query=myquery
"""

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def home(x_potato_header: str = Header(...)):
    return {"header": x_potato_header}
