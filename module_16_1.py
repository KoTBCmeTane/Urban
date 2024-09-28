from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

class User(BaseModel):
    username: str
    age: int

@app.get("/user")
def read_user_info(user: User):
    return {"message": f"Информация о пользователе. Имя: {user.username}, Возраст: {user.age}"}