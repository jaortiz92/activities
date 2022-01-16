from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

"""SQLALCHEMY_DATABASE_URL = "sqlite:///./activities.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
info = open("./config/configdb.json")
info = json.load(info)

engine = create_engine(
    f'postgresql://{info["user"]}:{info["pass"]}@{info["host"]}/{info["db"]}')

SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()
