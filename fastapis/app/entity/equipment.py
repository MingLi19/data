from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.entity.equipement_fuel import EquipmentFuel
from app.entity.vessel import Vessel
from app.model.equipment import EquipmentType

if TYPE_CHECKING:
    from app.entity.meta import FuelType


class Equipment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: EquipmentType

    created_at: datetime = Field(default_factory=datetime.utcnow)

    vessel_id: int = Field(default=None, foreign_key="vessel.id")
    vessel: Vessel | None = Relationship(back_populates="equipments")

    fuel_types: list["FuelType"] = Relationship(back_populates="equipments", link_model=EquipmentFuel)
