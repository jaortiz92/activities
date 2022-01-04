# FastApi
from fastapi import FastAPI

# App
from config import engine
from models import Base
from routes import activity, account

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Path Operations
app.include_router(activity)
app.include_router(account)
