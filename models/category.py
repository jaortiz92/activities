# SQLalchemy
from sqlalchemy import (
    Column, ForeignKey,
    Integer, String)
from sqlalchemy.orm import relationship
# APP
from config import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)

    group_id = Column(Integer, ForeignKey("groups.group_id"), nullable=False)
    group = relationship("Group", back_populates="categories")

    category = Column(String, nullable=False)
