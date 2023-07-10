from fastapi import APIRouter, Body

from src.bussiness import PatientBussiness
from src.presentation.schemas import Patient

patient = APIRouter(prefix="/api/v1/patient", tags=["patient"])


@patient.post("/", status_code=200, description="recive new patient")
def new_patient(patient: Patient = Body(..., description="patient data")):
    return PatientBussiness.insert(patient)