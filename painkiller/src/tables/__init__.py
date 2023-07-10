from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import DATABASE_URI

engine = create_engine(DATABASE_URI, echo=True)

class Base(DeclarativeBase):
    pass