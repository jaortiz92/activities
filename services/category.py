# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Category
import services
import schemas


def validate_foreign_keys(db: Session, category: schemas.CategoryCreate):
    db_group: models.Group = services.get_group(
        db, category.group_id)
    if not db_group:
        return "group"
    return None


def get_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(
        Category.category_id == category_id).first()
    if db_category:
        return db_category
    return None


def get_categories(db: Session):
    return db.query(Category).order_by(Category.category).all()


def get_categories_by_group(db: Session, group_id: int):
    db_category = db.query(Category).filter(
        Category.group_id == group_id).order_by(Category.category).all()
    if db_category:
        return db_category
    return None


def create_category(db: Session, category: schemas.CategoryCreate):
    validation = validate_foreign_keys(db, category)
    if validation:
        return validation
    db_category: Category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category: Category = get_category(db, category_id)
    if db_category:
        db_transaction = services.get_transactions_by_category(db, category_id)
        print(db_transaction)
        if not db_transaction:
            db.delete(db_category)
            db.commit()
            return f"Category with category_id {db_category.category_id} deleted"
        else:
            return f"Transactions"
    return None


def update_category(db: Session, category_id: int, category: schemas.CategoryCreate):
    validation = validate_foreign_keys(db, category)
    if validation:
        return validation
    db_category = db.query(Category).filter(
        Category.category_id == category_id
    )
    if db_category:
        db_category.update(category.dict())
        db.commit()
        return get_category(db, category_id)
    return None
