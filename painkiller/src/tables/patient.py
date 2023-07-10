from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.tables import Base
import src.tables.condition as condition

class Patient(Base):
    __tablename__ = "patient"

    parent_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    condition_id: Mapped[int] = mapped_column(ForeignKey("condition.condition_id"))

    condition: Mapped["condition.Condition"] = relationship(back_populates="patients")
