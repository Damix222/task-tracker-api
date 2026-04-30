from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []


@app.get("/")
def check_status():
    return {"message": "Task Tracker API is running"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(title: str, description: str):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "completed": False
    }

    tasks.append(task)

    return task


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")