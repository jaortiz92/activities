# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Group
import services
import schemas


def get_group(db: Session, group_id: int):
    db_group = db.query(Group).filter(
        Group.group_id == group_id).first()
    if db_group:
        return db_group
    return None