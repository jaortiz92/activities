# SQLalchemy
from sqlalchemy import (
    Column,
    Integer, String)
# APP
from config import Base


class Origin(Base):
    __tablename__ = "origins"

    origin_id = Column(Integer, primary_key=True,
                       index=True, autoincrement=True)

    origin = Column(String, nullable=False)
