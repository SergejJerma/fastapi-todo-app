from sqlalchemy.orm import Session
from models import ToDoDB

def create_todo(db: Session, todo: ToDoDB):
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
def update_todo(db: Session, todo_id: str, updated_data: dict):
    todo = db.query(ToDoDB).filter(ToDoDB.id == todo_id).first()
    if not todo:
        return None
    for key, value in updated_data.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo
def delete_todo(db: Session, todo_id: str):
    todo = db.query(ToDoDB).filter(ToDoDB.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo
