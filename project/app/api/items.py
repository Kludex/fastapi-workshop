from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models import Item

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/")
def create_item(name: str, price: int, session: Session = Depends(get_session)):
    """
    Create an item.

    \f
    Args:
        name (str): The name of the item.
        price (int): The price of the item.
        session (Session): The database session.

    Returns:
        dict: The item.
    """
    item = Item(name=name, price=price)
    session.add(item)
    session.commit()
    return item.dict()
