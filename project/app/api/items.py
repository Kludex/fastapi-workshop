from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth import authorized
from app.core.database import get_session
from app.models import Item
from app.schemas.items import ItemCreate, ItemOutput

router = APIRouter(prefix="/items", tags=["Items"], dependencies=[Depends(authorized)])


@router.get("/", response_model=list[ItemOutput])
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
    return items


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
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", status_code=201, response_model=ItemOutput)
def create_item(body: ItemCreate, session: Session = Depends(get_session)):
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
    item = Item(**body.dict())
    session.add(item)
    session.commit()
    return item


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
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
