# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
from schemas import Description
import services
from .utils import register_not_found, get_db


# Description
description = APIRouter(
    prefix="/description",
    tags=["Description"],
)


@description.get(
    path="/",
    response_model=List[Description],
    status_code=status.HTTP_200_OK,
    summary="Show all Description"
)
def show_all_descriptions(
    db: Session = Depends(get_db)
):
    """
    Show all Description

    This path operation show all descriptions in the app

    Parameters:
    - None

    Returns a json list with all descriptions in the app, with the following keys
    description_id: int,
    group: Group
    description: str
    """
    return services.get_descriptions(db)


@description.get(
    path="/{description_id}",
    response_model=Description,
    status_code=status.HTTP_200_OK,
    summary="Show a Description"
)
def show_a_description(
    description_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show a Description

    This path operation show a description in the app

    Parameters:
    - Register path parameter
        - description_id: int

    Returns a json with a description in the app, with the following keys
    description_id: int,
    group: Group
    description: str
    """
    response = services.get_description(db, description_id)
    if not response:
        register_not_found("Description")
    return response


@description.get(
    path="/group/{group_id}",
    response_model=List[Description],
    status_code=status.HTTP_200_OK,
    summary="Show Descriptions filter by group"
)
def show_descriptions_by_group(
    group_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show Descriptions filter by group

    This path operation show all descriptions in the app with a group selected

    Parameters:
    - Register path parameter
        - group_id: int

    Returns a json list with all descriptions in the app, with the following keys
    description_id: int,
    group: Group
    description: str
    """
    response = services.get_descriptions_by_group(db, group_id)
    if not response:
        register_not_found("Group in descriptions")
    return response
