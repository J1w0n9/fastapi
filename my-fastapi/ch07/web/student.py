from fastapi import APIRouter, Depends

from ch07.db_connect import Session, get_db
from ch07.schema.student import StudentResponse, Student
from ch07.service import student as service

router = APIRouter(prefix="/stu")

@router.post("", response_model= StudentResponse , status_code=201)
def create_student(data: Student, db: Session = Depends(get_db)):
    return service.create(db, data)
