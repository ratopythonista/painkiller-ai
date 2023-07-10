from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from painkiller.tables import Base
import painkiller.tables.patient as patient

class ConditionBase(Base):
    __tablename__ = "condition"

    condition_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    patients: Mapped[List["patient.PatientBase"]] = relationship(
        back_populates="condition", cascade="all, delete-orphan"
    )