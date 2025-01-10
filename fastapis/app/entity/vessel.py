from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.model.vessel import VesselBase

if TYPE_CHECKING:
    from app.entity.equipment import Equipment

from app.entity.company import Company
from app.entity.meta import ShipType, TimeZone


class Vessel(VesselBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    equipments: list["Equipment"] = Relationship(back_populates="vessel")

    company_id: int | None = Field(default=None, foreign_key="company.id")
    company: Company | None = Relationship(back_populates="vessels")

    ship_type_id: int | None = Field(default=None, foreign_key="ship_type.id")
    ship_type: ShipType | None = Relationship(back_populates="vessel")

    time_zone_id: int | None = Field(default=None, foreign_key="time_zone.id")
    time_zone: TimeZone | None = Relationship(back_populates="vessel")
