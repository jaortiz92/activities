# SQLalchemy
from sqlalchemy import (
    Column,
    Integer, String)
# APP
from config import Base


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True,
                      index=True, autoincrement=True)

    group = Column(String, nullable=False)
