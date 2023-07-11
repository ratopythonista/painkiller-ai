from enum import Enum
from pydantic import BaseModel, Field


class Patient(BaseModel):
    first_name: str = Field(..., description="Patient first name")
    second_name: str = Field(..., description="Patient second name")
    age: int = Field(..., description="Patient age", gt=0, lt=120)
    condition_id: int = Field(..., description="Patient Contidion Identifier")


class Condition(BaseModel):
    condition_id: int = Field(..., description="Patient Contidion Identifier")
    name: str = Field(..., description="Condition Name")

class DefaultResponse(BaseModel):
    request: str = Field(..., description="describre request service")
    response: str = Field(..., description="describe response from service requested")

