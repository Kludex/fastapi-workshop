"""
This example shows how to use body parameters.

To run this example, use the following command:

    uvicorn body_params:app --reload

And then open your browser at http://localhost:8000/docs.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


@app.post("/items/")
async def create_item(item: Item):
    return item
