from typing import List

from ch05.error import Duplicate
from ch05.model.todo import TodoResponse
from ch05.data import todo as todo_data
from ch05.model.todo import *
from ch06.classifier_random_regression import classify_content
from ch06.classifier_random_forest import classify_content as rf_classify_content
from ch06.nalmuk import predict_category


def find_all() -> List[TodoResponse]:
    return todo_data.find_all()

def create_one(todo : Todo) -> TodoResponse:
    #result = classify_content(todo.task)
    result2 = rf_classify_content(todo.task)
    #result3 = predict_category(todo.task)
    #print(result["predicted_category"])
    print(result2["predicted_category"])
    #print(result3["predicted_category"])
    return todo_data.create_one(todo)

def delete_one(todo_id: int) -> bool:
    if is_even(todo_id):
        return False
    else:
        return todo_data.delete_one(todo_id)

def completed_one(todo_id: int) -> TodoResponse:
    return todo_data.completed_one(todo_id)

def is_even(todo_id: int) -> bool:
    if todo_id % 2 == 0:
        return True
    return False