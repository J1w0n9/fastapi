from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    task: str

class TodoResponse(Todo):
    todo_id: int
    completed: bool
    created_at: datetime