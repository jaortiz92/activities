# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Origin
import services
import schemas


def get_origin(db: Session, origin_id: int):
    db_origin = db.query(Origin).filter(
        Origin.origin_id == origin_id).first()
    if db_origin:
        return db_origin
    return None


def get_origins(db: Session):
    return db.query(Origin).order_by(Origin.origin).all()
