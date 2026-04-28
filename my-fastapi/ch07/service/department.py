from fastapi import HTTPException

from ch07.data import department as d_data
from ch07.data.department import find_all
from ch07.db_connect import Session
from ch07.schema.department import DepartmentResponse, Department


def create(db : Session, dept : Department) -> DepartmentResponse:
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

    # 1. 학과가 존재하는가?
    if dept is None:
        raise HTTPException(status_code=404,
                            detail=f"학과가 존재하지 않습니다. 학과 id = {id}")
    # 학과 존재함
    # 2. 소속된 학생들이 있는가?
    if dept.students:
        raise HTTPException(status_code=409,
                            detail=f"소속학생이 있어 삭제할 수 없습니다. 학생: {len(dept.students)}")
    else:
        d_data.delete(db, id)
        return True

