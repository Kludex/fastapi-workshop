from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: int


class ItemCreate(ItemBase):
    """Data to create an item."""


class ItemOutput(ItemBase):
    """Output data for an item."""

    id: int

    class Config:
        """Model configuration."""

        orm_mode = True
