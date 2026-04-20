#추가하고싶은 라우터
from typing import List

from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse

from ch05.error import Duplicate
from ch05.model.todo import *
from ch05.service import todo as todo_service

router = APIRouter(prefix="/todo")

# 전체 조회
@router.get("")
def get_all() -> List[TodoResponse]:
    todos = todo_service.find_all()
    return todos

@router.post("")

async def create_one(todo:Todo) -> TodoResponse:
    try:
        return todo_service.create_one(todo)
    except Duplicate as err:
        raise HTTPException(status_code=404, detail=err.msg) from err

@router.delete("/{todo_id}")
async def delete_one(todo_id: int) -> bool:
    return todo_service.delete_one(todo_id)

@router.patch("/{todo_id}")
async def completed_one(todo_id: int) -> TodoResponse:
    return todo_service.completed_one(todo_id)