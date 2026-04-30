from fastapi import FastAPI, HTTPException
from app.schemas import TaskCreate, TaskResponse

app = FastAPI()

tasks = []


@app.get("/")
def check_status():
    return {"message": "Task Tracker API is running"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task_data: TaskCreate):
    task = {
        "id": len(tasks) + 1,
        "title": task_data.title,
        "description": task_data.description,
        "completed": False
    }

    tasks.append(task)

    return task


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")