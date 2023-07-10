from painkiller.tables import PatientBase
from painkiller.repository import Repository

class PatientRepository(Repository):
    def insert(patient: PatientBase) -> int:
        return Repository.insert(patient)
