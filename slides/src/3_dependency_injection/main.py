"""
This is an application that uses dependency injection.

You can run it with uvicorn:

    uvicorn main:app

And then visit http://localhost:8000/items/42 in your browser.
"""
from fastapi import Depends, FastAPI

app = FastAPI()


class Session:
    def query(self, item_id: str):
        return {"name": "foo", "id": item_id}

    def close(self):
        ...


def get_session():
    session = Session()
    yield session
    session.close()


@app.get("/items/{item_id}")
async def read_item(item_id: str, session: Session = Depends(get_session)):
    return session.query(item_id=item_id)
