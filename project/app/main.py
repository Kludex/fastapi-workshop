from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.database import engine, get_session
from app.models import Base, Item

app = FastAPI(title=get_settings().APP_NAME)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"Hello": "World"}


@app.post("/items/")
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
