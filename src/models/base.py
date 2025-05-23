from datetime import datetime
from typing import TypeVar
from pydantic import BaseModel as PydanticBaseModel

T = TypeVar('T')

class BaseModel(PydanticBaseModel):
    """Base model for all Pydantic models in the application."""
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
        extra = "forbid"
        validate_by_name = True