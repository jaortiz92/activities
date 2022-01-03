# SQLalchemy
from sqlalchemy import (
    Column,
    Integer, String)
from sqlalchemy.orm import relationship
# APP
from config import Base


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True,
                      index=True, autoincrement=True)
    group = Column(String, nullable=False)

    categories = relationship("Category", back_populates="group")
    descriptions = relationship("Description", back_populates="group")
    kinds = relationship("Kind", back_populates="group")
