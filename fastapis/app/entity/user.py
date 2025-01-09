from datetime import datetime

from app.entity.company import Company
from app.model.user import UserBase
from sqlmodel import Field, Relationship


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    company_id: int | None = Field(default=None, foreign_key="company.id")
    company: Company | None = Relationship(back_populates="users")
