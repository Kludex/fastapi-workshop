"""
This is a simple example of a WebSocket endpoint.

It accepts a WebSocket connection, sends a message, and then closes the connection.

You can test it with the following command:

    uvicorn ws:app --reload

And then using a WebSocket client like wscat:

    wscat -c ws://localhost:8000/ws
"""

from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello WebSocket!")
    await websocket.close()
