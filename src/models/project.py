from datetime import datetime
from typing import Optional

from pydantic import HttpUrl
from models.base import BaseModel


class Project(BaseModel):
    id: str
    name: str
    description: str = ""
    order: Optional[int] = None
    color: Optional[str] = None
    is_collapsed: bool = False
    is_favorite: bool = False
    is_archived: bool = False
    is_shared: bool = False
    created_at: datetime
    updated_at: datetime
    workspace_id: Optional[str] = None
    folder_id: Optional[str] = None
    url: Optional[HttpUrl] = None
    is_inbox_project: Optional[bool] = None
