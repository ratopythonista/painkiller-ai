from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.tables import Base
import src.tables.patient as patient

class Condition(Base):
    __tablename__ = "condition"

    condition_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    patients: Mapped[List["patient.Patient"]] = relationship(
        back_populates="condition", cascade="all, delete-orphan"
    )