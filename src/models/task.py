from datetime import datetime
from typing import Optional, List

from pydantic import Field
from models.base import BaseModel
from models.common import Due, Meta, Duration


class Task(BaseModel):
    """Task information."""
    id: str
    content: str
    description: Optional[str] = None
    is_completed: bool = False
    order: Optional[int] = None
    priority: int = 1
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    url: str
    project_id: str
    section_id: Optional[str] = None
    parent_id: Optional[str] = None
    duration: Optional[Duration]
    labels: List[str] = Field(default_factory=list)
    due: Optional[Due] = None
    meta: Optional[Meta] = None
    creator_id: Optional[str] = None
