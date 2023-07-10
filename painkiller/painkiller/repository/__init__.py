from sqlalchemy import select
from sqlalchemy.orm import Session, DeclarativeBase

from painkiller.tables import engine

class Repository:
    def insert(column: DeclarativeBase):
        with Session(engine) as session:
            session.add(column)
            session.commit()
            return True
        
    def get_by(column: DeclarativeBase, filter: bool):
        with Session(engine) as session:
            stmt = select(column).where(filter)
            return session.scalars(stmt).one()


    def get_all_by(column: DeclarativeBase, filter: bool):
        with Session(engine) as session:
            stmt = select(column).where(filter)
            return session.scalars(stmt).all() 

            
    def get_all(column: DeclarativeBase):
        with Session(engine) as session:
            stmt = select(column)
            return session.scalars(stmt).all()