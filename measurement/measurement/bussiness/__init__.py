from dataclasses import  asdict

from fastapi import HTTPException

from measurement.exception import ErrorMessage
from measurement.presentation.schemas import DefaultResponse

from painkiller.tables import PatientMeasurementBase
from painkiller.repository.patient import PatientRepository
from painkiller.repository.measurement import MeasurementRepository

class MeasurementBussiness:
    def insert(patient_id: int, measurement_id: int, value: float):
        if PatientRepository.insert_measurement(PatientMeasurementBase(patient=patient_id, measurement=measurement_id, value=value)):
            return DefaultResponse(request="Insert Patient Measurement", response="Success")
        else:
            raise HTTPException(**asdict(ErrorMessage.NOT_INSERTED.value))
        
    def get_all() -> list[dict]:
        return MeasurementRepository.get_all()
