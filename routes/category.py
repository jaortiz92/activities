# Python
from typing import List
from urllib import response

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
from schemas import Category, CategoryCreate
import services
from .utils import (
    register_not_found, get_db,
    if_error_redirect_category,
    register_with_transactions)


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


@category.get(
    path="/group/{group_id}",
    response_model=List[Category],
    status_code=status.HTTP_200_OK,
    summary="Show Categories filter by group"
)
def show_categories_by_group(
    group_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show Categories filter by group

    This path operation show all categories in the app with a group selected

    Parameters:
    - Register path parameter
        - group_id: int

    Returns a json list with all categories in the app, with the following keys
    category_id: int,
    group: Group
    category: str
    """
    response = services.get_categories_by_group(db, group_id)
    if not response:
        register_not_found("Group in categories")
    return response


@category.post(
    path="/post",
    response_model=Category,
    status_code=status.HTTP_201_CREATED,
    summary="Create a category"
)
def create_a_category(
    category: CategoryCreate = Body(...),
    db: Session = Depends(get_db)
):
    """
    Create a Category

    This path operation register a category in the app

    Parameters:
    - Register body parameter
        - group_id: int
        - category: str

    Retrurns a json with a category, with the following keys

    - category_id: int,
    - group_id: int,
    - category: str
    """
    response = services.create_category(db, category)
    if_error_redirect_category(response)
    return response


@category.delete(
    path="/{category_id}/delete",
    status_code=status.HTTP_200_OK,
    summary="Delete a category"
)
def delete_a_category(
    category_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Delete a Category

    This path operation delete a category

    Parameters:
    - Register path parameter
        - category_id: int

    Return a json with information about deletion
    """
    response = services.delete_category(db, category_id)
    if not response:
        register_not_found("Category")
    elif response == "Transactions":
        register_with_transactions("Category", category_id)
    return {"detail": response}
