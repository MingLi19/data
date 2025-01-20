from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from app.entity.company import Company


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    username: str = Field(unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    phone: str = Field(nullable=False)
    is_admin: bool = False
    is_system_admin: bool = False
    disabled: bool = False

    created_at: datetime = Field(default_factory=datetime.utcnow)

    company_id: int | None = Field(default=None, foreign_key="company.id")
    company: Company | None = Relationship(back_populates="users")
