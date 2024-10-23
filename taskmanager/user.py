from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/user', tags=['user'])

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

@router.get('/')
def all_users():
    pass

@router.get('/{user_id}')
def user_by_id(user_id: int):
    pass

@router.post('/create')
def create_user(user: CreateUser):
    pass

@router.put('/update')
def update_user(user: UpdateUser):
    pass

@router.delete('/delete')
def delete_user():
    pass