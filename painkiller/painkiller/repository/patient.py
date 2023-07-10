from painkiller.tables import PatientBase, PatientMeasurementBase
from painkiller.repository import Repository
from sqlalchemy.orm import DeclarativeBase

class PatientRepository(Repository):
    def insert(patient: PatientBase) -> int:
        return Repository.insert(patient)
    
    def insert_measurement(patient_mesurement: PatientMeasurementBase) -> int:
        return Repository.insert(patient_mesurement)

    def get_by_id(patient_id: int) -> PatientBase:
        return Repository.get_by(PatientBase, PatientBase.patient_id == patient_id)

    def get_all() -> list[PatientBase]:
        return Repository.get_all(PatientBase)
    
    def get_measurements(patient_id: int) -> list[PatientMeasurementBase]:
        return Repository.get_all_by(PatientMeasurementBase, PatientMeasurementBase.patient == patient_id)