import enum

from ch07.db_connect import Session
from ch07.model.student import Student, Gender

def insert(db: Session, name: str, gender : Gender, score : float, department_id : int, preferred_department_id : int):
    stu = Student(name = name, gender = gender, score = score, department_id = department_id, preferred_department_id = preferred_department_id)
    db.add(stu)
    db.commit()
    db.refresh(stu)
    return stu

def find_by_id(db: Session, id: int):
    return db.query(Student).filter(Student.id == id).first()