from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from painkiller.tables import Base
import painkiller.tables.condition as condition

class PatientBase(Base):
    __tablename__ = "patient"

    patient_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    condition_id: Mapped[int] = mapped_column(ForeignKey("condition.condition_id"))

    condition: Mapped["condition.ConditionBase"] = relationship(back_populates="patients")
