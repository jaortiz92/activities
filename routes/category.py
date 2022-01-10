# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
from schemas import Category
import services
from .utils import register_not_found, get_db


# Category
category = APIRouter(
    prefix="/category",
    tags=["Category"],
)


@category.get(
    path="/",
    response_model=List[Category],
    status_code=status.HTTP_200_OK,
    summary="Show all Categories"
)
def show_all_categories(
    db: Session = Depends(get_db)
):
    """
    Show all Categories

    This path operation show all categories in the app

    Parameters:
    - None

    Returns a json list with all categories in the app, with the following keys
    category_id: int,
    group: Group
    category: str
    """
    return services.get_categories(db)


@category.get(
    path="/{category_id}",
    response_model=Category,
    status_code=status.HTTP_200_OK,
    summary="Show a Category"
)
def show_a_category(
    category_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show a Category

    This path operation show a category in the app

    Parameters:
    - Register path parameter
        - category_id: int

    Returns a json with a category in the app, with the following keys
    category_id: int,
    group: Group
    category: str
    """
    response = services.get_category(db, category_id)
    if not response:
        register_not_found("Category")
    return response
