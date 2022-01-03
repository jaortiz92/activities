# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Group(BaseModel):
    group_id: int = Field(...)
    group: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    class Config:
        orm_mode = True
