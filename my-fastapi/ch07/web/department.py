from fastapi import APIRouter, Depends

from ch07.db_connect import Session, get_db
from ch07.schema.department import DepartmentResponse, Department
from ch07.service import department as service

router = APIRouter(prefix="/dept")

@router.post("", response_model= DepartmentResponse , status_code=201)
def create_department(data: Department, db: Session = Depends(get_db)):
    return service.create(db, data)

@router.get("", response_model= list[DepartmentResponse])
def get_all_departments(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.delete("/{id}") # /dept/3
def delete(db: Session = Depends(get_db), id: int = None) -> bool:
    return service.delete(db, id)