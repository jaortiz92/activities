# Python
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
#from .transaction import TransactionShow
from .account import Account
from config import Nature


class ActivityBase(BaseModel):
    nature: Nature = Field(...)
    transaction_id: int = Field(...)

    class Config:
        orm_mode = True


class ActivityCreate(ActivityBase):
    account_id: int = Field(...)


class ActivityShow(ActivityBase):
    activity_id: int = Field(...)
    #transaction: TransactionShow = Field(...)
    account: Account = Field(...)
    created_date: datetime = Field(...)
    updated_date: Optional[datetime] = Field(...)
