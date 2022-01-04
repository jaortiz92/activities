# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Transaction
import services
import schemas


def get_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(
        Transaction.transaction_id == transaction_id).first()
    if db_transaction:
        return db_transaction
    return None
