from fastapi import HTTPException

from ch07.data import student as s_data
from ch07.data import department as d_data
from ch07.db_connect import Session
from ch07.schema.student import StudentResponse, StudentCreate, StudentUpdate


def create(db : Session, stu : StudentCreate) -> StudentResponse:
   dept = d_data.find_by_id(db, stu.department_id)
   if not dept:
       raise HTTPException(status_code=404, detail="학과가 존재하지 않아요")
   if stu.preferred_department_id:
       preferred = d_data.find_by_id(db, stu.preferred_department_id)
       if not preferred:
           raise HTTPException(status_code=404, detail="희망 학과가 존재하지 않아요")
   s = s_data.insert(db, stu.name, stu.gender, stu.score, stu.department_id, stu.preferred_department_id)
   return StudentResponse.model_validate(s)

def get_all(db : Session):
    from ch07.data.student import find_all
    students = find_all(db)
    return [StudentResponse.model_validate(stu) for stu in students]


def get_by_dept_id(db, dept_id):
    dept = d_data.find_by_id(db, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="학과가 존재하지않음")
    student = s_data.get_by_dept_id(db, dept_id)
    return [StudentResponse.model_validate(s) for s in student]

def update_stu(db : Session, student_id : int, update_data: StudentUpdate):
    student = d_data.find_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="학생이 존재하지않음")
    update_fileds = update_data.model_dump(exclude_unset=True)  # -> 딕셔너리로 변환 **dic 사용하기 위해
    updated = d_data.update(db, student, **update_fileds)  # -> (db, dept, name, personnel)
    return StudentResponse.model_validate(updated)

def assign_dept(db : Session):
    depts = d_data.find_all_except_default(db)
    assigned_count = {dept.id: 0 for dept in depts}
    overflow_students = []

    for dept in depts:
        student = s_data.find_by_preferred_dept(db, dept.id)

        for i, student in enumerate(student):
            if i < dept.personnel:
                student.department_id = dept.id
                assigned_count[dept.id] += 1
                break
            else:
                overflow_students.append(student)
    for student in overflow_students:
        for dept in depts:
            remain = dept.personnel - assigned_count[dept.id]
            if remain > 0:
                student.department_id = dept.id
                assigned_count[dept.id] += 1
                break
    db.commit()
    return {"message": "학과 배정이 완료되었습니다."}