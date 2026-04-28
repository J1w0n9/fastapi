from fastapi import HTTPException

from ch07.data import student as s_data
from ch07.data import department as d_data
from ch07.db_connect import Session
from ch07.schema.student import StudentResponse, Student


def create(db : Session, stu : Student) -> StudentResponse:
   dept = d_data.find_by_id(db, stu.department_id)
   if not dept:
       raise HTTPException(status_code=404, detail="학과가 존재하지 않아요")
   if stu.preferred_department_id:
       preferred = d_data.find_by_id(db, stu.preferred_department_id)
       if not preferred:
           raise HTTPException(status_code=404, detail="희망 학과가 존재하지 않아요")
   s = s_data.insert(db, stu.name, stu.gender, stu.score, stu.department_id, stu.preferred_department_id)
   return StudentResponse.model_validate(s)