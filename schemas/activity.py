# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .transaction import Transaction
from .account import Account
from config import Nature


class ActivityBase(BaseModel):
    nature: Nature = Field(...)

    class Config:
        orm_mode = True


class ActivityCreate(ActivityBase):
    transaction_id: int = Field(...)
    account_id: int = Field(...)


class ActivityShow(ActivityBase):
    activity_id: int = Field(...)
    transaction: Transaction = Field(...)
    account: Account = Field(...)
    created_date: datetime = Field(...)
    updated_date: datetime = Field(...)
