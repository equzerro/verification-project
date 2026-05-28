from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from app.auth import verify_user

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    email: EmailStr

@app.post("/register")
def register(user: User):
    if len(user.password) < 8:
        raise HTTPException(status_code=400, detail="Weak password")

    return {
        "status": "success",
        "user": user.username
    }

@app.post("/login")
def login(user: User):
    verified = verify_user(user.username, user.password)

    if not verified:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "token": "demo-jwt-token"
    }