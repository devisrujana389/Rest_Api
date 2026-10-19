from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# The shape of data we expect when creating or updating a user
class User(BaseModel):
    name: str
    email: str


# Temporary storage (a list in memory, no database needed)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"}
]
next_id = 2  # counter so ids are never reused after a delete


# GET: read all users
@app.get("/users")
def get_users():
    return users


# GET: read one user by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# POST: create a new user
@app.post("/users", status_code=201)
def create_user(user: User):
    global next_id
    new_user = {"id": next_id, "name": user.name, "email": user.email}
    next_id += 1
    users.append(new_user)
    return new_user


# PUT: update (replace) an existing user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    for existing in users:
        if existing["id"] == user_id:
            existing["name"] = user.name
            existing["email"] = user.email
            return existing
    raise HTTPException(status_code=404, detail="User not found")


# DELETE: remove a user
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return
    raise HTTPException(status_code=404, detail="User not found")
