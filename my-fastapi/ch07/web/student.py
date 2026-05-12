from fastapi import APIRouter, Depends

from ch07.db_connect import Session, get_db
from ch07.schema.student import StudentResponse, StudentCreate, StudentUpdate
from ch07.service import student as service

router = APIRouter(prefix="/stu")

@router.post("", response_model= StudentResponse , status_code=201)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    return service.create(db, data)

@router.get("", response_model= list[StudentResponse] , status_code=200)
def all_student(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/{dept_id}/students", response_model= list[StudentResponse] , status_code=200)
def get_students_by_dept(dept_id: int, db: Session = Depends(get_db)):
    return service.get_by_dept_id(db, dept_id)

@router.put("/{student_id}", response_model= StudentResponse , status_code=200)
def update_stu(student_id: int,data:StudentUpdate, db: Session = Depends(get_db)):
    return service.update_stu(db, student_id, data)