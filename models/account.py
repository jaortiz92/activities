# SQLalchemy
from sqlalchemy import (
    Column, ForeignKey,
    Integer, String)
from sqlalchemy.orm import relationship
# APP
from config import Base


class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)

    class_account_id = Column(Integer, ForeignKey(
        "classes_account.class_account_id"), nullable=False)
    class_account = relationship("ClassAccount", back_populates="accounts")

    account = Column(String, nullable=False)

    activities = relationship("Activity", back_populates="account")
