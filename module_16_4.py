from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
def get_all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
def create_user(user: User, username: str, age: int):
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int, user: str = Body()):
    try:
        edit_user = users[user_id-1]
        for edit_user in users:
            if edit_user.id == user_id:
                edit_user.username = username
                edit_user.age = age
                return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    try:
        delete_user = users[user_id - 1]
        for delete_user in users:
            if delete_user.id == user_id:
                users.pop(user_id-1)
                return delete_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


