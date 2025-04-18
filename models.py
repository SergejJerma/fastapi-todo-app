from typing import List, Optional
from pydantic import BaseModel
class ToDo(BaseModel):
    id: str
    title: str
    description: Optional[str] = None