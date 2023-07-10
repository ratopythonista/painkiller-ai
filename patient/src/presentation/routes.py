from fastapi import APIRouter, Body

from src.bussiness import PatientBussiness, ConditionBussiness
from src.presentation.schemas import Patient, DefaultResponse, Condition

patient = APIRouter(prefix="/api/v1/patient", tags=["patient"])


@patient.post("/", status_code=200, description="recive new patient", response_model=DefaultResponse)
def new_patient(patient: Patient = Body(..., description="patient data")):
    return PatientBussiness.insert(patient)

@patient.get("/{patient_id}", status_code=200, description="get pacient info", response_model=Patient)
def get_patient(patient_id: int):
    return PatientBussiness.get_by_id(patient_id)

@patient.get("/conditions", description="list all conditions", response_model=list[Condition])
def get_all_conditions():
    return ConditionBussiness.get_all()