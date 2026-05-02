# Task Tracker API

Task Tracker API — учебный backend-проект для управления задачами через REST API.

Проект позволяет создавать задачи, получать список задач, получать задачу по id, обновлять задачу, менять статус выполнения и удалять задачу. Данные сохраняются в SQLite базе данных.

## Стек

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

## Возможности

- Создание задачи
- Получение списка задач
- Получение задачи по id
- Обновление задачи
- Изменение статуса задачи
- Удаление задачи
- Хранение данных в SQLite
- Автоматическая документация через Swagger

## Структура проекта

```text
task_tracker_api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── __init__.py
│       └── tasks.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <>
cd task_tracker_api
```

### 2. Создать виртуальное окружение

Для Windows PowerShell:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустить сервер

```bash
uvicorn app.main:app --reload
```

После запуска API будет доступно по адресу:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get task by id |
| PUT | `/tasks/{task_id}` | Update task |
| PATCH | `/tasks/{task_id}/complete` | Mark task as completed |
| DELETE | `/tasks/{task_id}` | Delete task |


## Скриншоты

Примеры:

```text
images/swagger_main.png
images/create_task.png
images/get_tasks.png
images/update_task.png
images/delete_task.png
```

## Что я изучил

В процессе работы над проектом я изучил:

- базовую структуру FastAPI-проекта;
- создание REST API endpoints;
- работу с HTTP-методами GET, POST, PUT, PATCH, DELETE;
- использование Pydantic-схем для request и response;
- подключение SQLite базы данных;
- основы SQLAlchemy ORM;
- создание моделей базы данных;
- работу с database session;
- разделение проекта на `routers`, `crud`, `models`, `schemas` и `database`;
- обработку ошибок через `HTTPException`;
- тестирование API через Swagger.
