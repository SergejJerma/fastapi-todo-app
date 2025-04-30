from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, ToDo, ToDoDB
import queries
import commands

app = FastAPI()
Base.metadata.create_all(bind=engine)  # Create DB table
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=list[ToDo])
def read_todos(db: Session = Depends(get_db)):
    return queries.get_all_todos(db)

@app.get("/todos/{todo_id}", response_model=ToDo)
def read_todo(todo_id: str, db: Session = Depends(get_db)):
    todo = queries.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@app.post("/todos", response_model=ToDo)
def create_todo(todo: ToDo, db: Session = Depends(get_db)):
    db_todo = ToDoDB(**todo.model_dump())
    return commands.create_todo(db, db_todo)

@app.put("/todos/{todo_id}", response_model=ToDo)
def update_todo(todo_id: str, updated_todo: ToDo, db: Session = Depends(get_db)):
    todo = commands.update_todo(db, todo_id, updated_todo.model_dump())
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str, db: Session = Depends(get_db)):
    todo = queries.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    commands.delete_todo(db, todo_id)
    return {"message": "ToDo deleted successfully"}