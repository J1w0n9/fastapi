from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Depends
from uvicorn import lifespan

from ch07.db_connect import Base, engine, Session, get_db
from ch07.model import student, department


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

@app.get("/")
def index(db: Session = Depends(get_db)):
    # 객체 생성해서 db.add -> db.commit 해서 실제로 들어갔는지 확인
    dept = department(name = "공통학과", personnel = 64)
    db.add(dept)
    db.commit()
    return {"message": "department assignment system"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)