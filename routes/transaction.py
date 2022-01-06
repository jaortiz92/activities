# Python
from datetime import datetime
from typing import Dict, List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
#from schemas import Message, MessageCreate

from schemas import (
    TransactionCreate, TransactionShow,
    TransactionCompleteCreate, ActivityCreate
)
import services
from .utils import (
    register_not_found, if_error_redirect_transaction,
    get_db, if_error_redirect_activity, validate_cr_and_db
)

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
    if_error_redirect_transaction(response)
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
    if_error_redirect_transaction(response)
    return response


@transaction.post(
    path="/complete_post",
    response_model=TransactionShow,
    status_code=status.HTTP_200_OK,
    summary="Create a Transaction and Activites"
)
def create_an_transaction_and_activities(
    transactionComplete: TransactionCompleteCreate = Body(...),
    db: Session = Depends(get_db)
):
    """
    Create a Transaction and its Activites

    This path operation register a transaction and its activities in the app

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
        - activity_one: Activity
        - activity_two: Activity

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
    transactionComplete: Dict = transactionComplete.dict()
    activity_one = transactionComplete.pop("activity_one")
    activity_two = transactionComplete.pop("activity_two")
    validate_cr_and_db(activity_one, activity_two)

    transaction = TransactionCreate(**transactionComplete)
    response = create_a_transaction(transaction, db)
    transaction_id = response.transaction_id

    activity_one["transaction_id"] = transaction_id
    activity_one = ActivityCreate(
        **activity_one
    )
    response_activity_one = services.create_activity(db, activity_one)
    if isinstance(response_activity_one, str):
        services.delete_transaction(db, transaction_id)
        if_error_redirect_activity(response_activity_one)

    activity_two["transaction_id"] = transaction_id
    activity_two = ActivityCreate(
        **activity_two
    )
    response_activity_two = services.create_activity(db, activity_two)
    if isinstance(response_activity_two, str):
        services.delete_activity(db, response_activity_one.activity_id)
        services.delete_transaction(db, transaction_id)
        if_error_redirect_activity(response_activity_two)
    return services.get_transaction(db, transaction_id)
