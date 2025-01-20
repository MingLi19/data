from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.entity.user import User
    from app.entity.vessel import Vessel


class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False)
    address: str | None = None
    contact_person: str | None = None
    contact_phone: str | None = None
    contact_email: str | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)

    users: list["User"] = Relationship(back_populates="company")
    vessels: list["Vessel"] = Relationship(back_populates="company")
