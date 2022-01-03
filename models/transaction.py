# Python
from datetime import date, datetime
# SQLalchemy
from sqlalchemy import (
    Boolean, Column, ForeignKey,
    Integer, String, Date, DateTime)
from sqlalchemy.orm import relationship
# APP
from config import Base


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True,
                            index=True, autoincrement=True)
    transaction_date = Column(Date, nullable=False)

    category_id = Column(Integer, ForeignKey(
        "categories.category_id"), nullable=False)
    category = relationship("Category", back_populates="transactions")

    description_id = Column(Integer, ForeignKey(
        "descriptions.description_id"), nullable=False)
    description = relationship("Description", back_populates="transactions")

    kind_id = Column(Integer, ForeignKey("kinds.kind_id"), nullable=False)
    kind = relationship("Kind", back_populates="transactions")

    origin_id = Column(Integer, ForeignKey(
        "origins.origin_id"), nullable=False)
    origin = relationship("Origin", back_populates="transactions")

    activities = relationship("Activity", back_populates="transaction")

    value = Column(Integer, nullable=False)
    detail = Column(String)
    created_date = Column(DateTime, default=datetime.now(), nullable=False)
    updated_date = Column(DateTime, default=None,
                          onupdate=datetime.now(), nullable=True)
