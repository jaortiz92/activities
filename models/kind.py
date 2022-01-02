# SQLalchemy
from sqlalchemy import (
    Column, ForeignKey,
    Integer, String)
from sqlalchemy.orm import relationship
# APP
from config import Base


class Kind(Base):
    __tablename__ = "kinds"

    kind_id = Column(Integer, primary_key=True,
                     index=True, autoincrement=True)

    group_id = Column(Integer, ForeignKey("groups.group_id"), nullable=False)
    group = relationship("Group", back_populates="kinds")

    kind = Column(String, nullable=False)
