# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .group import Group


class Description(BaseModel):
    description_id: int = Field(...)
    group: Group = Field(...)
    description: str = Field(...)

    class Config:
        orm_mode = True
