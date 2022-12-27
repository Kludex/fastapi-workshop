"""
This is an application that uses data validation.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str
    price: float


class ItemOutput(Item):
    item_id: int


@app.post("/items/", response_model=ItemOutput)
def create_item(item: Item):
    item.de  # This line fails!
    return {"item_id": 42, **item.dict()}
