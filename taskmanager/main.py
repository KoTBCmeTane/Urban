from fastapi import FastAPI
from task import router as task_router
from user import router as user_router

app = FastAPI()

app.include_router(task_router)
app.include_router(user_router)

@app.get('/')
def read_root():
    return {"message": "Welcome to Taskmanager"}