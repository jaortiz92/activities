# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
from .utils import (get_db)
import services
from schemas import DepositAccount

# Query
query = APIRouter(
    prefix="/query",
    tags=["Queries"],
)


@query.get(
    path="/deposit_accounts",
    response_model=List[DepositAccount],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Show values of deposit accounts"
)
def show_deposit_accounts(
    db: Session = Depends(get_db)
):
    """
    Show deposit accounts

    This path operation show values of deposit accounts

    Paramters:
    - None

    Retrurns
    - deposit_account: str
    - value: int
    """
    return services.get_desposit_accounts(db)
