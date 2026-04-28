from pydantic import BaseModel, ConfigDict


class Department(BaseModel):
    name : str
    personnel : int

class DepartmentResponse(Department):
    model_config = ConfigDict(from_attributes=True)
    id : int
