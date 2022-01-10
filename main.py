# FastApi
from fastapi import FastAPI

# App
from config import engine
from models import Base
from routes import (
    activity, account, transaction, category,
    description, kind, origin
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url="/"
)

# Path Operations
app.include_router(transaction)
app.include_router(activity)
app.include_router(account)
app.include_router(category)
app.include_router(description)
app.include_router(kind)
app.include_router(origin)
