from fastapi import FastAPI, HTTPException
from models import ToDo
import crud
app = FastAPI()

@app.get("/todos", response_model=list[ToDo])
def read_todos():
    return crud.get_all_todos()

@app.get("/todos/{todo_id}", response_model=ToDo)
def read_todo(todo_id: int):
    todo = crud.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@app.post("/todos", response_model=ToDo)
def create_todo(todo: ToDo):
    return crud.create_todo(todo)

@app.put("/todos/{todo_id}", response_model=ToDo)
def update_todo(todo_id: int, updated_todo: ToDo):
    todo = crud.update_todo(todo_id, updated_todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if not crud.get_todo(todo_id):
        raise HTTPException(status_code=404, detail="ToDo not found")
    crud.delete_todo(todo_id)
    return {"message": "ToDo deleted successfully"}