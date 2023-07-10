from typing import List

from sqlalchemy import String, ForeignKey, create_engine, Integer
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship

from painkiller.config import DATABASE_URI

engine = create_engine(DATABASE_URI, echo=True)

class Base(DeclarativeBase):
    pass


class PatientBase(Base):
    __tablename__ = "patient"

    patient_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer())
    condition_id: Mapped[int] = mapped_column(ForeignKey("condition.condition_id"))

    condition: Mapped["ConditionBase"] = relationship(back_populates="patients")


class ConditionBase(Base):
    __tablename__ = "condition"

    condition_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    patients: Mapped[List["PatientBase"]] = relationship(
        back_populates="condition", cascade="all, delete-orphan"
    )