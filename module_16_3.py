from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def read_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(username: Annotated[str, Path(description="Enter username", examples={"value": "UrbanUser"}, min_length=5, max_length=20)],
                age: Annotated[int, Path(description="Enter age", examples={"value": 24}, ge=18, le=120)]):
    user_id = str(max(int(key) for key in users) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[str, Path(description="Enter user ID", examples={"value": "1"})],
                username: Annotated[str, Path(description="Enter username", examples={"value": "UrbanProfi"}, min_length=5, max_length=20)],
                age: Annotated[int, Path(description="Enter age", examples={"value": 28}, ge=18, le=120)]):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        return f"User {user_id} not found"

@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[str, Path(description="Enter user ID", examples={"value": "1"})]):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        return f"User {user_id} not found"