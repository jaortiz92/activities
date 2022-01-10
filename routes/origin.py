# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
from schemas import Origin
import services
from .utils import register_not_found, get_db


# Origin
origin = APIRouter(
    prefix="/origin",
    tags=["Origin"],
)


@origin.get(
    path="/",
    response_model=List[Origin],
    status_code=status.HTTP_200_OK,
    summary="Show all Categories"
)
def show_all_origins(
    db: Session = Depends(get_db)
):
    """
    Show all Categories

    This path operation show all origins in the app

    Parameters:
    - None

    Returns a json list with all origins in the app, with the following keys
    origin_id: int,
    origin: str
    """
    return services.get_origins(db)


@origin.get(
    path="/{origin_id}",
    response_model=Origin,
    status_code=status.HTTP_200_OK,
    summary="Show a Origin"
)
def show_a_origin(
    origin_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show a Origin

    This path operation show a origin in the app

    Parameters:
    - Register path parameter
        - origin_id: int

    Returns a json with a origin in the app, with the following keys
    origin_id: int,
    origin: str
    """
    response = services.get_origin(db, origin_id)
    if not response:
        register_not_found("Origin")
    return response
