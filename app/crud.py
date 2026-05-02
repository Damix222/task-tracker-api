from sqlalchemy.orm import Session

from app import models
from app.schemas import TaskCreate, TaskUpdate


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def create_task(db: Session, task_data: TaskCreate):
    db_task = models.Task(
        title=task_data.title,
        description=task_data.description,
        completed=False
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    db_task = get_task(db, task_id)

    if db_task is None:
        return None

    db_task.title = task_data.title
    db_task.description = task_data.description
    db_task.completed = task_data.completed

    db.commit()
    db.refresh(db_task)

    return db_task


def complete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)

    if db_task is None:
        return None

    db_task.completed = True

    db.commit()
    db.refresh(db_task)

    return db_task


def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)

    if db_task is None:
        return None

    db.delete(db_task)
    db.commit()

    return db_task