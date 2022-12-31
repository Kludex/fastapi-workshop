from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models import Item

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def get_items(session: Session = Depends(get_session)):
    """
    Get all items.

    \f
    Args:
        session (Session): The database session.

    Returns:
        list: The items.
    """
    items = session.query(Item).all()
    return [item.dict() for item in items]


@router.get("/{item_id}")
def get_item(item_id: int, session: Session = Depends(get_session)):
    """
    Get an item.

    \f
    Args:
        item_id (int): The ID of the item.
        session (Session): The database session.

    Returns:
        dict: The item.
    """
    item = session.query(Item).get(item_id)
    return item.dict()


@router.post("/", status_code=201)
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


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, session: Session = Depends(get_session)):
    """
    Delete an item.

    \f
    Args:
        item_id (int): The ID of the item.
        session (Session): The database session.
    """
    item = session.query(Item).get(item_id)
    session.delete(item)
    session.commit()
