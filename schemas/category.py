# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .group import Group


class CategoryBase(BaseModel):
    category: str = Field(...)

    class Config:
        orm_mode = True

class CategoryCreate(CategoryBase):
    group_id: int = Field(..., gt=0)

class Category(CategoryBase):
    group: Group = Field(...)
    category_id: int = Field(...)