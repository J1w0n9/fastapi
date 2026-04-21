from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ch07.db_connect import Base
from ch07.model.student import Student


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    personal = Column(Integer)

    students = relationship(
        "Student",
        back_populates="department",
        foreign_keys="Student.department_id"
    )

    preferred_students = relationship(
        "Student",
        back_populates="preferred_department",
        foreign_keys="Student.preferred_department_id"
    )