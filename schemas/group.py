# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Group(BaseModel):
    group_id: int = Field(...)
    group: str = Field(...)

    class Config:
        orm_mode = True
