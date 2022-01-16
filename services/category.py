# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Category
import services
import schemas


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
