# Python
from datetime import datetime

# SQLalchemy
from sqlalchemy import (
    Column, ForeignKey, Enum,
    Integer, DateTime)
from sqlalchemy.orm import relationship
# APP
from config import Base
from config import Nature


class Activity(Base):
    __tablename__ = "activities"

    activity_id = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)

    transaction_id = Column(Integer, ForeignKey(
        "transactions.transaction_id", ondelete='CASCADE'), nullable=False)
    transaction = relationship("Transaction", back_populates="activities")

    account_id = Column(Integer, ForeignKey(
        "accounts.account_id"), nullable=False)
    account = relationship("Account", back_populates="activities")

    nature = Column(Enum(Nature), nullable=False)

    created_date = Column(DateTime, default=datetime.now(), nullable=False)
    updated_date = Column(DateTime, default=None,
                          onupdate=datetime.now(), nullable=True)
