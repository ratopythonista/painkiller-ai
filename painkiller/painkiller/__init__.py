from painkiller.tables import Base, engine

def create_database():
    Base.metadata.create_all(engine)