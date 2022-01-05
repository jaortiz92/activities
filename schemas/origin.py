# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Origin(BaseModel):
    origin_id: int = Field(...)
    origin: str = Field(...)

    class Config:
        orm_mode = True
