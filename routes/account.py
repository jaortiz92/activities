# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
from schemas import Account
import services
from .utils import register_not_found, get_db


# Account
account = APIRouter(
    prefix="/account",
    tags=["Account"],
)


@account.get(
    path="/",
    response_model=List[Account],
    status_code=status.HTTP_200_OK,
    summary="Show all Accounts"
)
def show_all_accounts(
    db: Session = Depends(get_db)
):
    """
    Show all Accounts

    This path operation show all accounts in the app

    Parameters:
    -

    Returns a json list with all accounts in the app, with the following keys
    - "account_id": int,
    - "class_account": {
        - "class_account_id": int,
        - "nature": int,
        - "class_account": str
    },
    - "account": str
    """
    return services.get_accounts(db)


@account.get(
    path="/{account_id}",
    response_model=Account,
    status_code=status.HTTP_200_OK,
    summary="Show a Account"
)
def show_an_account(
    account_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show an Account

    This path operation show an account in the app

    Parameters:
    - Register path parameter
        - account_id: int

    Returns a json with an account in the app, with the following keys
    - "account_id": int,
    - "class_account": {
        - "class_account_id": int,
        - "nature": int,
        - "class_account": str
    },
    - "account": str   
    """
    response = services.get_account(db, account_id)
    if not response:
        register_not_found("Account")
    return response
