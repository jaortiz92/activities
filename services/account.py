# Python
from typing import List
from sqlalchemy.orm import Session

# App
import models
from models import Account
import services
import schemas


def get_account(db: Session, account_id: int):
    db_account = db.query(Account).filter(
        Account.account_id == account_id).first()
    if db_account:
        return db_account
    return None


def get_accounts(db: Session):
    return db.query(Account).all()
