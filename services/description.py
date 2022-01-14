# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Description
import services
import schemas


def get_description(db: Session, description_id: int):
    db_description = db.query(Description).filter(
        Description.description_id == description_id).first()
    if db_description:
        return db_description
    return None


def get_descriptions(db: Session):
    return db.query(Description).all()


def get_descriptions_by_group(db: Session, group_id: int):
    db_description = db.query(Description).filter(
        Description.group_id == group_id).all()
    if db_description:
        return db_description
    return None
