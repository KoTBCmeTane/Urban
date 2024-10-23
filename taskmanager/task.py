from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/task', tags=['task'])

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int

@router.get('/')
def all_tasks():
    pass

@router.get('/{task_id}')
def task_by_id(task_id: int):
    pass

@router.post('/create')
def create_task(task: CreateTask):
    pass

@router.put('/update')
def update_task(task: UpdateTask):
    pass

@router.delete('/delete')
def delete_task():
    pass