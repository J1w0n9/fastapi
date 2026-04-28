from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from ch07.db_connect import Base, engine
from ch07.web import department as department_web
from ch07.web import student as student_web

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 서버의 시작과 끝
    Base.metadata.create_all(engine)
    print("[서버 시작] DB 테이블 생성")
    yield
    print("[서버 끝] 종료")

app = FastAPI(
    lifespan=lifespan
)

app.include_router(department_web.router)
app.include_router(student_web.router)
@app.get("/")
def index():
    return {"message": "department assignment system"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)