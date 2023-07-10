from dataclasses import  asdict

from fastapi import HTTPException

from src.exception import ErrorMessage
from src.presentation.schemas import Patient, DefaultResponse

from painkiller.tables import PatientBase
from painkiller.repository.patient import PatientRepository
from painkiller.repository.condition import ConditionRepository

class PatientBussiness:
    def insert(patient: Patient):
        patient_dict = patient.model_dump()
        patient_dict["condition_id"] = ConditionRepository.get_by_name(patient.condition.value).condition_id
        del patient_dict["condition"]

        if PatientRepository.insert(PatientBase(**patient_dict)):
            return DefaultResponse(request="Insert Patient", response="Success")
        else:
            raise HTTPException(**asdict(ErrorMessage.NOT_INSERTED))