from typing import List, Optional
from models import ToDo

todo_list: List[ToDo] = []
def get_all_todos() -> List[ToDo]:
    return todo_list
def get_todo(todo_id: str) -> Optional[ToDo]:
    return next((todo for todo in todo_list if todo.id == todo_id), None)
