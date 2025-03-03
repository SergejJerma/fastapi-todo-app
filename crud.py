from typing import List, Optional
from models import ToDo

todo_list: List[ToDo] = []

def get_all_todos() -> List[ToDo]:
    return todo_list

def get_todo(todo_id: int) -> Optional[ToDo]:
    return next((todo for todo in todo_list if todo.id == todo_id), None)

def create_todo(todo: ToDo) -> ToDo:
    todo_list.append(todo)
    return todo

def update_todo(todo_id: int, updated_todo: ToDo) -> Optional[ToDo]:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    return None

def delete_todo(todo_id: int) -> bool:
    global todo_list
    todo_list = [todo for todo in todo_list if todo.id != todo_id]
    return True
