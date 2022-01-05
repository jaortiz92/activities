# Python
from datetime import datetime
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session
from models.transaction import Transaction

# App
#from schemas import Message, MessageCreate

from schemas import TransactionCreate, TransactionShow
import services
from .exceptions import register_not_found
from .dependency import get_db

transaction = APIRouter(
    prefix="/transaction",
    tags=["Transaction"],
)


@transaction.get(
    path="/",
    response_model=List[TransactionShow],
    status_code=status.HTTP_200_OK,
    summary="Show all transactions"
)
def show_all_transactions(
    db: Session = Depends(get_db)
):
    """
    Show all Activities

    This path operation show all activities in the app

    Paramters:
    - 

    Retrurns a json list with all activities, with the following keys
    transaction_date: date,
    - value: int,
    - detail: str,
    - transaction_id: int,
    - category: Category
    - description: Description
    - kind: Kind,
    - origin: Origin,
    - destiny: Destiny,
    - activities: [Activity],
    - created_date: datetime,
    - updated_date: datetime
    """
    return services.get_transactions(db, 0, 100)


@transaction.get(
    path="/{transaction_id}",
    response_model=TransactionShow,
    status_code=status.HTTP_200_OK,
    summary="Show a transaction"
)
def show_a_transaction(
    transaction_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show a Transaction

    This path operation show a transaction in the app

    Paramters:
    - Register path parameter
        - transaction_id: int

    Retrurns a json with a transaction, with the following keys
    transaction_date: date,
    - value: int,
    - detail: str,
    - transaction_id: int,
    - category: Category
    - description: Description
    - kind: Kind,
    - origin: Origin,
    - destiny: Destiny,
    - activities: [Activity],
    - created_date: datetime,
    - updated_date: datetime
    """
    response = services.get_transaction(db, transaction_id)
    if not response:
        register_not_found("Transaction")
    return response


@transaction.post(
    path="/post",
    response_model=TransactionShow,
    status_code=status.HTTP_201_CREATED,
    summary="Create a Transaction"
)
def create_a_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    """
    Create a Transaction

    This path operation register a transaction in the app

    Parameters:
    - Register body parameter
        - transaction_date: date,
        - value: int,
        - detail: str,
        - category_id: int,
        - description_id: int,
        - kind_id: int,
        - origin_id: int,
        - destiny_id: int

    Retrurns a json with a transaction, with the following keys
    - value: int,
    - detail: str,
    - transaction_id: int,
    - category: Category
    - description: Description
    - kind: Kind,
    - origin: Origin,
    - destiny: Destiny,
    - activities: [Activity],
    - created_date: datetime,
    - updated_date: datetime
    """
    response = services.create_transaction(db, transaction)
    if response == "category":
        register_not_found("Category")
    if response == "description":
        register_not_found("Description")
    if response == "kind":
        register_not_found("Kind")
    if response == "origin":
        register_not_found("Origin")
    if response == "destiny":
        register_not_found("Destiny")
    return response


@transaction.delete(
    path="/{transaction_id}/delete",
    status_code=status.HTTP_200_OK,
    summary="Delete a Transaction",
)
def delete_a_transaction(
    transaction_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Delete a Transaction

    This path operation delete a transaction

    Parameters:
    - Register path parameter
        - transaction_id: int

    Return a json with information about deletion
    """
    response = services.delete_transaction(db, transaction_id)
    if not response:
        register_not_found("Transaction")
    return response


@transaction.put(
    path="/{transaction_id}/update",
    response_model=TransactionShow,
    status_code=status.HTTP_200_OK,
    summary="Update a Transaction"
)
def update_a_transaction(
    transaction_id: int = Path(..., gt=0),
    transaction: TransactionCreate = Body(...),
    db: Session = Depends(get_db)
):
    """
    Update a Transaction

    This path operation update a transaction in the app

    Parameters:
    - Register path parameter
        - transaction_id: int
    - Register body parameter
        - transaction_date: date,
        - value: int,
        - detail: str,
        - category_id: int,
        - description_id: int,
        - kind_id: int,
        - origin_id: int,
        - destiny_id: int

    Retrurns a json with a transaction, with the following keys
    - value: int,
    - detail: str,
    - transaction_id: int,
    - category: Category
    - description: Description
    - kind: Kind,
    - origin: Origin,
    - destiny: Destiny,
    - activities: [Activity],
    - created_date: datetime,
    - updated_date: datetime
    """
    response = services.update_transaction(db, transaction_id, transaction)
    if response == "category":
        register_not_found("Category")
    if response == "description":
        register_not_found("Description")
    if response == "kind":
        register_not_found("Kind")
    if response == "origin":
        register_not_found("Origin")
    if response == "destiny":
        register_not_found("Destiny")
    return response
