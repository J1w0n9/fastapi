
from fastapi import FastAPI
from pydantic import *
from typing import Optional

app = FastAPI()

users = []

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=4)
    age: int = Field(..., gt=0)
    email: EmailStr

@app.post("/sign-up")
def sign_up(user: User):
    users.append(user)

    return f"{user.name}님이 입장하셨습니다."


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("sign-up:app", host="0.0.0.0", port=8000)