import enum
from sqlalchemy import *
from sqlalchemy.orm import relationship
from ch07.db_connect import Base


class Gender(enum.Enum):
    Male = "male"
    Female = "female"

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    score = Column(Float, nullable=False, default=0.0)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    preferred_department_id = Column(Integer, ForeignKey("department.id"), nullable=False)

    department = relationship(
        "Department",
        back_populates="students",
        foreign_keys=[department_id]
    )

    preferred_department = relationship(
        "Department",
        back_populates="preferred_students",
        foreign_keys=[preferred_department_id]
    )

