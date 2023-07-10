from src.tables import Base, engine
from src.tables.patient import Patient # NOQA
from src.tables.condition import Condition # NOQA

def create_all():
    Base.metadata.create_all(engine)