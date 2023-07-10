from dataclasses import  asdict

from fastapi import HTTPException

from src.exception import ErrorMessage
from src.presentation.schemas import Patient, DefaultResponse

from painkiller.tables import PatientBase
from painkiller.repository.patient import PatientRepository
from painkiller.repository.condition import ConditionRepository

class PatientBussiness:
    def insert(patient: Patient):
        if PatientRepository.insert(PatientBase(**patient.model_dump())):
            return DefaultResponse(request="Insert Patient", response="Success")
        else:
            raise HTTPException(**asdict(ErrorMessage.NOT_INSERTED))
        
class ConditionBussiness:
    def get_all():
        return ConditionRepository.get_all()