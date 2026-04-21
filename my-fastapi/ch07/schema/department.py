from pydantic import BaseModel, ConfigDict


class Department(BaseModel):
    name : str
    personal : str

class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int