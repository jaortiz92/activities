# FastApi
from fastapi import FastAPI

# App
from config import engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
