from enum import Enum
from pydantic import BaseModel, Field


class Condition(Enum):
    HEALTHY = "Healthy"
    PRESSURE = "High blood pressure"
    DIABETE = "Diabetes"
    HEAT_DISEASE = "Heart disease"
    ASTHMA = "Asthma"
    OBESITY = "Obesity"
    ARTHRITIS = "Arthritis"
    ALZHEIMER = "Alzheimer's"
    DEPRESSION = "Depression"


class Patient(BaseModel):
    first_name: str = Field(..., description="Patient first name")
    second_name: str = Field(..., description="Patient second name")
    age: int = Field(..., description="Patient age", gt=0, lt=120)
    condition: Condition = Field(..., description="Patient Contidion")

class DefaultResponse(BaseModel):
    request: str = Field(..., description="describre request service")
    response: str = Field(..., description="describe response from service requested")