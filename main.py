# FastApi
from fastapi import FastAPI

# App
from config import engine
from models import Base
from routes import activity

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Path Operations
app.include_router(activity)
