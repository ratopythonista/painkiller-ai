from fastapi import APIRouter, Body

from measurement.bussiness import MeasurementBussiness
from measurement.presentation.schemas import DefaultResponse, Measurement

measurement = APIRouter(prefix="/api/v1", tags=["patient"])


@measurement.post("/patient/{patient_id}/measurements", status_code=200, description="set pacient measurement info", response_model=DefaultResponse)
def get_patient(patient_id: int, measurement_id: int, value: float):
    return MeasurementBussiness.insert(patient_id, measurement_id, value)

@measurement.get("/measurements", description="list all measurements", response_model=list[Measurement])
def get_all_conditions():
    return MeasurementBussiness.get_all()