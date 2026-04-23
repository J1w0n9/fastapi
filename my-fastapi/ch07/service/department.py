from fastapi import HTTPException

from ch07.data import department as d_data
from ch07.db_connect import Session
from ch07.schema.department import DepartmentResponse, Department


def create(db : Session, dept : Department) -> DepartmentResponse:
    exisiting_department = d_data.find_by_name(db, dept.name)
    if exisiting_department:
        raise HTTPException(status_code=409, detail="학과 이름이 이미 존재해요.")
    dept = d_data.insert(db, dept.name, dept.personnel)
    return DepartmentResponse.model_validate(dept)
