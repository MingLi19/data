from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.model.company import CompanyBase

if TYPE_CHECKING:
    from app.model.user import User
    from app.model.vessel import Vessel


class Company(CompanyBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    users: list["User"] = Relationship(back_populates="company")
    vessels: list["Vessel"] = Relationship(back_populates="company")
