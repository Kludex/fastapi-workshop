from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def notify_user():
    print("Sending email to user...")


@app.get("/")
async def home(background_tasks: BackgroundTasks):
    background_tasks.add_task(notify_user)
    return {"message": "Hello World"}
