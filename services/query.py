# Python
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func, text


def get_desposit_accounts(db: Session):
    db_query = db.execute(
        text("SELECT * FROM deposit_accounts")).all()
    result_query = []
    for row in db_query:
        result_query.append({
            "deposit_account": row[0],
            "value": row[1]
        })
    return result_query
