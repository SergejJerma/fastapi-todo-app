from typing import List, Optional
from pydantic import BaseModel
class ToDo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None