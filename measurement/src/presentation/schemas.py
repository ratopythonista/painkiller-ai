from enum import Enum
from pydantic import BaseModel, Field


class PatientMeasurement(BaseModel):
    patient: int = Field(..., description="Patient Identifier")
    measurement: int = Field(..., description="Measurement Identifier")
    value: float = Field(..., description="Value for that measurement for this pacient")


class Measurement(BaseModel):
    measurement_id: int = Field(..., description="Measurement Identifier")
    name: str = Field(..., description="Measurement Name")
    magnitude: str = Field(..., description="Measurement Magnitude")

class DefaultResponse(BaseModel):
    request: str = Field(..., description="describre request service")
    response: str = Field(..., description="describe response from service requested")

