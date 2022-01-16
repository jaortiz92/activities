# Python
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func

# App
import models
from models import Transaction
import services
import schemas


def validate_foreign_keys(db: Session, transaction: schemas.TransactionCreate):
    db_category: models.Category = services.get_category(
        db, transaction.category_id)
    if not db_category:
        return "category"
    db_description: models.Description = services.get_description(
        db, transaction.description_id)
    if not db_description:
        return "description"
    db_kind: models.Kind = services.get_kind(db, transaction.kind_id)
    if not db_kind:
        return "kind"
    db_origin: models.Origin = services.get_origin(db, transaction.origin_id)
    if not db_origin:
        return "origin"
    db_destiny: models.Origin = services.get_origin(db, transaction.destiny_id)
    if not db_destiny:
        return "destiny"
    return None


def get_transaction(db: Session, transaction_id: int):
    db_transaction: Transaction = db.query(Transaction).filter(
        Transaction.transaction_id == transaction_id).first()
    if db_transaction:
        return db_transaction
    return None


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Transaction).order_by(Transaction.transaction_date.desc(),
                                          Transaction.transaction_id.desc()
                                          ).offset(skip).limit(limit).all()


def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    validation = validate_foreign_keys(db, transaction)
    if validation:
        return validation
    db_transaction: Transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_transaction(db: Session, transaction_id: int):
    db_transaction: Transaction = services.get_transaction(db, transaction_id)
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return f"Transaction with transaction_id {db_transaction.transaction_id} deleted"
    return None


def update_transaction(db: Session, transaction_id: int, transaction: schemas.TransactionCreate):
    validation = validate_foreign_keys(db, transaction)
    if validation:
        return validation
    db_transaction = db.query(Transaction).filter(
        Transaction.transaction_id == transaction_id)
    if db_transaction:
        db_transaction.update(transaction.dict())
        db.commit()
        return get_transaction(db, transaction_id)
    return None


def count_transactions(db: Session):
    return db.query(func.count(Transaction.transaction_id)).scalar()
