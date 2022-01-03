# Python
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .category import Category
from .description import Description
from .kind import Kind
from .origin import Origin
#from .activity import ActivityShow


class TransactionBase(BaseModel):
    transaction_date: date = Field(...)
    value: int = Field(...)
    detail: Optional[str] = Field(default=None)

    class Config:
        orm_mode = True


class TransactionCreate(TransactionBase):
    category_id: int = Field(...)
    description_id: int = Field(...)
    kind_id: int = Field(...)
    origin_id: int = Field(...)


class TransactionShow(TransactionBase):
    transaction_id: int = Field(...)
    category: Category = Field(...)
    description: Description = Field(...)
    kind: Kind = Field(...)
    origin: Origin = Field(...)
    #activities: List[ActivityShow] = Field(...)
    created_date: datetime = Field(...)
    updated_date: Optional[datetime] = Field(...)
