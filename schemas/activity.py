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
    transaction_id: int = Field(..., gt=0)

    class Config:
        orm_mode = True


class ActivityCreate(ActivityBase):
    account_id: int = Field(..., gt=0)


class ActivityShow(ActivityBase):
    activity_id: int = Field(...)
    #transaction: TransactionShow = Field(...)
    account: Account = Field(...)
    created_date: datetime = Field(...)
    updated_date: Optional[datetime] = Field(...)


class ActivityCompleteCreate(ActivityCreate):
    transaction_id: Optional[int] = Field(default=None, gt=0)


class ActivityShowFront(BaseModel):
    nature: str = Field(...)
    account_id: int = Field(..., gt=0)
    activity_id: int = Field(..., gt=0)
