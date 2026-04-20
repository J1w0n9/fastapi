from sqlite3 import IntegrityError
from typing import List

from ch05.data import DBConnect
from ch05.error import Duplicate
from ch05.model.todo import TodoResponse, Todo

db = DBConnect()
cur = db.conn.cursor()

cur.execute("""
    create table if not exists todos(
        todo_id integer primary key autoincrement,
        task text not null unique,
        completed boolean not null default false,
        created_at timestamptz not null default (datetime('now', 'localtime'))
    )
""")

def find_all() -> List[TodoResponse]:
    query = "select * from todos"
    cur.execute(query)
    return [TodoResponse(**dict(row)) for row in cur.fetchall()]

def create_one(todo : Todo) -> TodoResponse:
    query = f"insert into todos (task) values ('{todo.task}')"
    try:
        cur.execute(query)
        db.commit()
    except IntegrityError as err:
        raise Duplicate("할 일 중복해서 입력하지 마라.")
    todo_id = cur.lastrowid
    # todo_id로 조회한 그 값을 TodoResponse로 리턴
    cur.execute(f"select * from todos where todo_id={todo_id}")
    return TodoResponse(**dict(cur.fetchone()))

def delete_one(todo_id: int) -> bool:
    query = f"delete from todos where todo_id={todo_id}"
    cur.execute(query)
    db.commit()
    return True

def completed_one(todo_id: int) -> TodoResponse:
    query = f"update todos set completed=not completed where todo_id={todo_id}"
    cur.execute(query)
    db.commit()
    cur.execute(f"select * from todos where todo_id={todo_id}")
    return TodoResponse(**dict(cur.fetchone()))