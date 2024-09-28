from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(user_id: Annotated[int, Path(description="Enter User ID", examples={"value": 1}, ge=1, le=100)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def read_user(username: Annotated[str, Path(description="Enter username", examples={"value": "UrbanUser"}, min_length=5, max_length=20)],
              age: Annotated[int, Path(description="Enter age", examples={"value": 24}, ge=18, le=120)]):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}