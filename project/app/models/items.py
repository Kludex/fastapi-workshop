from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Item(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
