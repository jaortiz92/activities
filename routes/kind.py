# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
from schemas import Kind
import services
from .utils import register_not_found, get_db


# Kind
kind = APIRouter(
    prefix="/kind",
    tags=["Kind"],
)


@kind.get(
    path="/",
    response_model=List[Kind],
    status_code=status.HTTP_200_OK,
    summary="Show all Kinds"
)
def show_all_kinds(
    db: Session = Depends(get_db)
):
    """
    Show all Kinds

    This path operation show all kinds in the app

    Parameters:
    - None

    Returns a json list with all kinds in the app, with the following keys
    kind_id: int,
    group: Group
    kind: str
    """
    return services.get_kinds(db)


@kind.get(
    path="/{kind_id}",
    response_model=Kind,
    status_code=status.HTTP_200_OK,
    summary="Show a Kind"
)
def show_a_kind(
    kind_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show a Kind

    This path operation show a kind in the app

    Parameters:
    - Register path parameter
        - kind_id: int

    Returns a json with a kind in the app, with the following keys
    kind_id: int,
    group: Group
    kind: str
    """
    response = services.get_kind(db, kind_id)
    if not response:
        register_not_found("Kind")
    return response


@kind.get(
    path="/group/{group_id}",
    response_model=List[Kind],
    status_code=status.HTTP_200_OK,
    summary="Show Kinds filter by group"
)
def show_kinds_by_group(
    group_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show Kinds filter by group

    This path operation show all kinds in the app with a group selected

    Parameters:
    - Register path parameter
        - group_id: int

    Returns a json list with all kinds in the app, with the following keys
    kind_id: int,
    group: Group
    kind: str
    """
    response = services.get_kinds_by_group(db, group_id)
    if not response:
        register_not_found("Group in kinds")
    return response
