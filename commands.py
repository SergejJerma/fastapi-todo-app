from typing import List
from models import ToDo
import queries

def create_todo(todo: ToDo) -> ToDo:
    queries.todo_list.append(todo)
    return todo

def update_todo(todo_id: str, updated_todo: ToDo) -> ToDo | None:
    for index, todo in enumerate(queries.todo_list):
        if todo.id == todo_id:
            queries.todo_list[index] = updated_todo
            return updated_todo
    return None

def delete_todo(todo_id: str) -> bool:
    queries.todo_list = [todo for todo in queries.todo_list if todo.id != todo_id]
    return True
