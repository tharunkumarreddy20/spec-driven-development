from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users_db = []

@app.get("/")
def health_check():
    return {"message": "FastAPI is running successfully"}

@app.post("/users", status_code=201)
def create_user(user: User):
    if any(u["id"] == user.id for u in users_db):
        raise HTTPException(status_code=400, detail="User already exists")
    users_db.append(user.model_dump())
    return user

@app.get("/users")
def get_users():
    return users_db