from pydantic import BaseModel, ConfigDict
from typing import Optional

class DepartmentCreate(BaseModel):
    name : str
    personnel : int

class DepartmentResponse(DepartmentCreate):
    model_config = ConfigDict(from_attributes=True)
    id : int

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    personnel: Optional[int] = None
