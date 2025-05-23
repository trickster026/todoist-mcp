from models.base import BaseModel
from typing import Optional


class Label(BaseModel):
    id: str
    name: str
    color: Optional[str] = None
    order: Optional[int] = None
    is_favorite: Optional[bool] = False