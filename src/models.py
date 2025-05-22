from typing import Optional
from pydantic import BaseModel


class TasksOutput(BaseModel):
    id: str
    content: str
    due_date: Optional[str] = None
    
