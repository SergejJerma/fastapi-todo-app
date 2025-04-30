from sqlalchemy.orm import Session
from models import ToDoDB

def get_all_todos(db: Session):
    return db.query(ToDoDB).all()
def get_todo(db: Session, todo_id: str):
    return db.query(ToDoDB).filter(ToDoDB.id == todo_id).first()