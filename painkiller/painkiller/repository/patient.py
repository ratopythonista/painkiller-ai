from painkiller.tables import PatientBase
from painkiller.repository import Repository

class PatientRepository(Repository):
    def insert(patient: PatientBase) -> int:
        return Repository.insert(patient)
    
    def get_by_id(patient_id: int) -> PatientBase:
        return Repository.get_by(PatientBase, PatientBase.patient_id == patient_id)
