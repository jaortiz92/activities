# SQLalchemy
from sqlalchemy import (
    Column, ForeignKey,
    Integer, String)
from sqlalchemy.orm import relationship
# APP
from config import Base


class Description(Base):
    __tablename__ = "descriptions"

    description_id = Column(Integer, primary_key=True,
                            index=True, autoincrement=True)

    group_id = Column(Integer, ForeignKey("groups.group_id"), nullable=False)
    group = relationship("Group", back_populates="descriptions")

    description = Column(String, nullable=False)
    transactions = relationship("Transaction", back_populates="description")
