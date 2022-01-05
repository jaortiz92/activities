# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .group import Group


class Kind(BaseModel):
    kind_id: int = Field(...)
    group: Group = Field(...)
    kind: str = Field(...)

    class Config:
        orm_mode = True
