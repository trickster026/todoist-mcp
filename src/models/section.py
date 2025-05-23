from typing import Optional
from models.base import BaseModel


class Section(BaseModel):
    id: str
    name: str
    project_id: str
    is_collapsed: Optional[bool] = False
    order: Optional[int] = None
