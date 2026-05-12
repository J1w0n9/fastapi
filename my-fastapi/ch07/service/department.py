from fastapi import HTTPException

from ch07.data import department as d_data
from ch07.data.department import find_all
from ch07.db_connect import Session
from ch07.schema.department import DepartmentResponse, DepartmentCreate, DepartmentUpdate
from ch07.schema.student import StudentResponse


def create(db : Session, dept : DepartmentCreate) -> DepartmentResponse:
    exisiting_department = d_data.find_by_name(db, dept.name)
    if exisiting_department:
        raise HTTPException(status_code=409, detail="학과 이름이 이미 존재해요.")
    dept = d_data.insert(db, dept.name, dept.personnel)
    return DepartmentResponse.model_validate(dept)

def get_all(db: Session):
    departments = find_all(db)
    return [DepartmentResponse.model_validate(dept) for dept in departments]

def delete(db: Session, id: int) -> bool:
    dept = d_data.find_by_id(db, id)
    if dept is None:
        raise HTTPException(status_code=404,
                            detail=f"학과가 존재하지 않습니다. 학과 id = {id}")
    if dept.students:
        raise HTTPException(status_code=409,
                            detail=f"소속학생이 있어 삭제할 수 없습니다. 학생: {len(dept.students)}")
    else:
        d_data.delete(db, id)
        return True

def get_students(db: Session, dept_id : int):
    dept = d_data.find_by_id(db, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="학과가 존재하지 않음")
    return [StudentResponse.model_validate(s) for s in dept.students]

def update_dept(db: Session, dept_id: int, update_data: DepartmentUpdate):
    dept = d_data.find_by_id(db, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail=f"해당하는 학과를 찾을 수 없음!!! id ={dept_id}")
    existing = d_data.find_by_name(db, update_data.name)
    if existing:
        raise HTTPException(status_code=409, detail="이미 존재하는 학과명입니다.")
    update_fileds = update_data.model_dump(exclude_unset=True) # -> 딕셔너리로 변환 **dic 사용하기 위해
    updated = d_data.update(db, dept, **update_fileds) # -> (db, dept, name, personnel)
    return DepartmentResponse.model_validate(updated)