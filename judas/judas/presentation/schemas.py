from enum import Enum
from pydantic import BaseModel, Field


class PredictData(BaseModel):
    age: int = Field(..., description="Patient age")
    blood_pressure: int = Field(..., description="Patient Bload Pressure")
    heart_rate: int = Field(..., description="Patient Hear Rate")
    breathing_rate: int = Field(..., description="Patient Breathing Rate")
    body_temperature: int = Field(..., description="Patient Body Temperature")
    oxygen_saturation: int = Field(..., description="Patient Oxygen Saturation")
    blood_glucose: int = Field(..., description="Patient Blood Glucose")
    sleep: int = Field(..., description="Patient Sleept")
    activity: int = Field(..., description="Patient Activity")
