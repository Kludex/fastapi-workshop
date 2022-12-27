"""
This application uses path parameters.

You can run it with uvicorn:

    uvicorn path_params:app

And then visit http://localhost:8000/your_name in your browser.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
def home(name: str):
    return {"Hello": name}
