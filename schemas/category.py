# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .group import Group


class Category(BaseModel):
    category_id: int = Field(...)
    group: Group = Field(...)
    category: str = Field(...)

    class Config:
        orm_mode = True
