from pydantic import BaseModel, ConfigDict


class Department(BaseModel):
    name : str
    personnel : int

class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
