# Pydantic
from pydantic import BaseModel
from pydantic import Field


class DepositAccount(BaseModel):
    deposit_account: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    value: int = Field(...)
