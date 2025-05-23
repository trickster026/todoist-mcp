from datetime import date, datetime
from typing import Literal, Optional, Union

from models.base import BaseModel

ApiDate = datetime
ApiDue = Union[date, datetime]
DurationUnit = Literal['minute', 'day']


class Due(BaseModel):
    """Due date information for tasks."""
    date:ApiDate 
    string: str
    lang: str = "en"
    is_recurring: Optional[bool] = False
    timezone: Optional[str] = None


class Duration(BaseModel):
    """Duration information for tasks."""
    amount: int
    unit: DurationUnit


class Deadline(BaseModel):
    """Deadline information for tasks."""
    date: ApiDate
    lang: str = "en"


class Meta(BaseModel):
    """Metadata for tasks."""
    project: tuple[str, str]
    section: tuple[str, str]
    assignee: tuple[str, str]
    labels: dict[int, str]
    due: Optional[Due] = None
    deadline: Optional[Deadline] = None
