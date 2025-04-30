from pydantic import BaseModel, ConfigDict
from typing import Optional
from sqlalchemy import Column, Integer, String
from database import Base

class ToDoDB(Base):
    __tablename__ = "todos"
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True)
    description: Optional[str] = Column(String, nullable=True)

class ToDo(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)