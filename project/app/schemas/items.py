from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: int


class ItemCreate(ItemBase):
    """Data to create an item."""
