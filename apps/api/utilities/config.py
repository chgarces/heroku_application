from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# import logging

# from flask import _app_ctx_stack
# import enum


Base = declarative_base()
engine = create_engine("sqlite:///hcms_db")
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=True, bind=engine),
)
# scopefunc=_app_ctx_stack.__ident_func__)
session = SessionLocal()
