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

def find_all(db:Session):
    return db.query(Student).all()

def get_by_dept_id(db : Session, dept_id: int):
    return db.query(Student).filter(Student.department_id == dept_id)

def update(db: Session, student:Student, **kwargs):
    for key, value in kwargs.items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student

def find_by_preferred_dept(db: Session, preferred_department_id: int):
    return (db.query(Student)
            .filter(Student.preferred_department_id == preferred_department_id)
            .order_by(Student.score.desc())
            .all()
            )