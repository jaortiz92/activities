# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Description
import services
import schemas


def validate_foreign_keys(db: Session, description: schemas.DescriptionCreate):
    db_group: models.Group = services.get_group(
        db, description.group_id)
    if not db_group:
        return "group"
    return None


def get_description(db: Session, description_id: int):
    db_description = db.query(Description).filter(
        Description.description_id == description_id).first()
    if db_description:
        return db_description
    return None


def get_descriptions(db: Session):
    return db.query(Description).order_by(Description.description).all()


def get_descriptions_by_group(db: Session, group_id: int):
    db_description = db.query(Description).filter(
        Description.group_id == group_id).order_by(Description.description).all()
    if db_description:
        return db_description
    return None


def create_description(db: Session, description: schemas.DescriptionCreate):
    validation = validate_foreign_keys(db, description)
    if validation:
        return validation
    db_description: Description = Description(**description.dict())
    db.add(db_description)
    db.commit()
    db.refresh(db_description)
    return db_description


def delete_description(db: Session, description_id: int):
    db_description: Description = get_description(db, description_id)
    if db_description:
        db_transaction = services.get_transactions_by_description(
            db, description_id)
        if not db_transaction:
            db.delete(db_description)
            db.commit()
            return f"Description with description_id {db_description.description_id} deleted"
        else:
            return f"Transactions"
    return None


def update_category(db: Session, description_id: int, description: schemas.DescriptionCreate):
    validation = validate_foreign_keys(db, description)
    if validation:
        return validation
    db_description = db.query(Description).filter(
        Description.description_id == description_id
    )
    if db_description:
        db_description.update(description.dict())
        db.commit()
        return get_description(db, description_id)
    return None
