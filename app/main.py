from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def check_stutus():
    return{'message': "Task Tracker API is running"}

