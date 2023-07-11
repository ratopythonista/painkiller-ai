from painkiller.tables import MeasurementBase
from painkiller.repository import Repository

class MeasurementRepository(Repository):
    def get_all() -> list[dict]:
        return Repository.get_all(MeasurementBase)