# Pydantic
from pydantic import BaseModel
from pydantic import Field

# App
from config import Nature


class ClassAcount(BaseModel):
    class_account_id: int = Field(...)
    nature: Nature = Field(...)
    class_account: str = Field(...)

    class Config:
        orm_mode = True
