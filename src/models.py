import datetime
from typing import Optional
from pydantic import BaseModel


class TasksOutput(BaseModel):
    id: str
    content: str
    due_date: Optional[str] = None


class ProjectsOutput(BaseModel):
    id: str
    name: str
    description: str
    is_favorite: bool
    is_archived: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    workspace_id: Optional[str] = None
    folder_id: Optional[str] = None
