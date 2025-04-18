from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ToDo
import queries
import commands

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos", response_model=list[ToDo])
def read_todos():
    return queries.get_all_todos()

@app.get("/todos/{todo_id}", response_model=ToDo)
def read_todo(todo_id: str):
    todo = queries.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@app.post("/todos", response_model=ToDo)
def create_todo(todo: ToDo):
    return commands.create_todo(todo)

@app.put("/todos/{todo_id}", response_model=ToDo)
def update_todo(todo_id: str, updated_todo: ToDo):
    updated_todo.id = todo_id
    todo = commands.update_todo(todo_id, updated_todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    if not queries.get_todo(todo_id):
        raise HTTPException(status_code=404, detail="ToDo not found")
    commands.delete_todo(todo_id)
    return {"message": "ToDo deleted successfully"}