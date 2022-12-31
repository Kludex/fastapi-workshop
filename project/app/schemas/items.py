from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., example="Kludex", description="The name of the item.")
    price: int = Field(..., example=100, description="The price of the item.")


class ItemCreate(ItemBase):
    """Data to create an item."""


class ItemOutput(ItemBase):
    """Output data for an item."""

    id: int = Field(..., example=1, description="The ID of the item.")

    class Config:
        """Model configuration."""

        orm_mode = True
