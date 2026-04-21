from pydantic import BaseModel, ConfigDict, Field

from ch07.model.student import Gender


class Student(BaseModel):
    name: str
    gender: Gender
    score : float = Field(default=0.0, ge=0.0, le=100.0)
    department_id: int
    preferred_department_id: int

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int