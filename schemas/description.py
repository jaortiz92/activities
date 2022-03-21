# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .group import Group


class DescriptionBase(BaseModel):
    description: str = Field(...)

    class Config:
        orm_mode = True


class DescriptionCreate(DescriptionBase):
    group_id: int = Field(..., gt=0)


class Description(DescriptionBase):
    group: Group = Field(...)
    description_id: int = Field(...)
