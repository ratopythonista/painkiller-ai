from sqlalchemy.orm import Session, DeclarativeBase

from src.tables import engine

class Repository:
    def insert(column: DeclarativeBase):
        with Session(engine) as session:
            session.add(column)