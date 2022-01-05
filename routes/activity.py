# Python
from datetime import datetime
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
#from schemas import Message, MessageCreate

from schemas import ActivityCreate, ActivityShow
import services
from .exceptions import register_not_found
from .dependency import get_db


# Activity
activity = APIRouter(
    prefix="/activity",
    tags=["Activity"],
)


@activity.get(
    path="/",
    response_model=List[ActivityShow],
    status_code=status.HTTP_200_OK,
    summary="Show all Activities"
)
def show_all_activities(
    db: Session = Depends(get_db)
):
    """
    Show all Activities

    This path operation show all activities in the app

    Paramters:
    - 

    Retrurns a json list with all activities, with the following keys

    - nature: int,
    - transaction_id: int,
    - activity_id: int,
    - account: Acount
    - created_date: datetime,
    - updated_date: datetime
    """
    return services.get_activities(db, 0, 100)


@activity.get(
    path="/{activity_id}",
    response_model=ActivityShow,
    status_code=status.HTTP_200_OK,
    summary="Show a activity"
)
def show_an_activity(
    activity_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Show a activity

    This path operation show an activity in the app

    Parameters:
    - Register path parameter
        - activity_id: int

    Retrurns a json with an activity, with the following keys

    - nature: int,
    - transaction_id: int,
    - activity_id: int,
    - account: Acount
    - created_date: datetime,
    - updated_date: datetime
    """
    response = services.get_activity(db, activity_id)
    if not response:
        register_not_found("Activity")
    return response


@activity.post(
    path="/post",
    response_model=ActivityShow,
    status_code=status.HTTP_201_CREATED,
    summary="Create an activity"
)
def create_an_activity(
    activity: ActivityCreate = Body(...),
    db: Session = Depends(get_db)
):
    """
    Create an Activity

    This path operation register an activity in the app

    Parameters:
    - Register body parameter
        - nature: int
        - transaction_id: int
        - account_id: int

    Retrurns a json with an activity, with the following keys

    - nature: int,
    - transaction_id: int,
    - activity_id: int,
    - account: Acount
    - created_date: datetime,
    - updated_date: datetime
    """
    response = services.create_activity(db, activity)
    if response == "transaction":
        register_not_found("Transaction")
    if response == "account":
        register_not_found("Account")
    return response


@activity.delete(
    path="/{activity_id}/delete",
    status_code=status.HTTP_200_OK,
    summary="Delete an Activity"
)
def delete_an_activity(
    activity_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    """
    Delete an Activity

    This path operation delete an activity

    Parameters:
    - Register path parameter
        - activity_id: int

    Return a json with information about deletion
    """
    response = services.delete_activity(db, activity_id)
    if not response:
        register_not_found("Activity")
    return {"detail": response}


@activity.put(
    path="/{activity_id}/update",
    response_model=ActivityShow,
    status_code=status.HTTP_200_OK,
    summary="Update an Activity"
)
def update_an_activity(
    activity_id: int = Path(..., gt=0),
    activity: ActivityCreate = Body(...),
    db: Session = Depends(get_db)
):
    """
    Update an Activity

    This path operation update an activity

    Parameters:
    - Register path parameter
        - activity_id: int
    - Register body parameter
        - nature: int
        - transaction_id: int
        - account_id: int

    Retrurns a json with an activity, with the following keys

    - nature: int,
    - transaction_id: int,
    - activity_id: int,
    - account: Acount
    - created_date: datetime,
    - updated_date: datetime
    """
    response = services.update_activity(db, activity_id, activity)
    if not response:
        register_not_found("Activity")
    if response == "transaction":
        register_not_found("Transaction")
    if response == "account":
        register_not_found("Account")
    return response
