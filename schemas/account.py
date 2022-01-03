# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from .classAcount import ClassAcount


class Account(BaseModel):
    account_id: int = Field(...)
    class_account: ClassAcount = Field(...)
    account: str = Field(...)

    class Config:
        orm_mode = True
