# Python
from datetime import datetime
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends, HTTPException
from fastapi import Body, Path
from sqlalchemy.orm.session import Session

# App
#from schemas import Message, MessageCreate
from config import SessionLocal
from schemas import ActivityCreate, ActivityShow
import services


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
    return services.get_activities(db, 0, 100)
