from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from app.models.company import Company


class UserBase(SQLModel):
    name: str
    username: str = Field(unique=True, nullable=False)
    hashed_password: str
    phone: str
    is_admin: bool
    is_system_admin: bool
    disabled: bool


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    company_id: int | None = Field(default=None, foreign_key="company.id")
    company: Company | None = Relationship(back_populates="users")


class UserCreate(UserBase):
    company_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Jayzhu",
                    "username": "jayzhu",
                    "hashed_password": "123456789",
                    "phone": "12345678999",
                    "is_admin": True,
                    "is_system_admin": False,
                    "disabled": False,
                    "company_id": 1,
                }
            ]
        }
    }


class UserUpdate(UserBase):
    company_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Jayzhu Updated",
                    "username": "jayzhu",
                    "hashed_password": "123456789",
                    "phone": "12345678999",
                    "is_admin": True,
                    "is_system_admin": False,
                    "disabled": False,
                    "company_id": 1,
                }
            ]
        }
    }


class UserWithCompany(UserBase):
    company: Company
