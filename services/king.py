# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Kind
import services
import schemas


def get_kind(db: Session, kind_id: int):
    db_kind = db.query(Kind).filter(
        Kind.kind_id == kind_id).first()
    if db_kind:
        return db_kind
    return None


def get_kinds(db: Session):
    return db.query(Kind).all()


def get_kinds_by_group(db: Session, group_id: int):
    db_kind = db.query(Kind).filter(
        Kind.group_id == group_id).all()
    if db_kind:
        return db_kind
    return None
