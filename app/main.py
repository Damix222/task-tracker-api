from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import tasks


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)


@app.get("/")
def check_status():
    return {"message": "Task Tracker API is running"}