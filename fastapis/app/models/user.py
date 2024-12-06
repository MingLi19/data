from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str = Field(unique=True, nullable=False)
    hashed_password: str | None
    phone: str | None
    is_admin: bool | None
    is_system_admin: bool | None
    disabled: bool | None
    created_at: datetime | None
    company_id: int | None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "username": "Jayzhu",
                    "hashed_password": "123456789",
                    "phone": "12345678999",
                    "is_admin": True,
                    "is_system_admin": False,
                    "disabled": False,
                    "created_at": "2024-12-01",
                    "company_id": 101,
                }
            ]
        }
    }


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "username": "Jayzhu",
                    "hashed_password": "123456789",
                    "phone": "12345678999",
                    "is_admin": True,
                    "is_system_admin": False,
                    "disabled": False,
                    "created_at": "2024-12-01",
                    "company_id": 101,
                }
            ]
        }
    }


class UserUpdate(BaseModel):
    username: str | None
    hashed_password: str | None
    phone: str | None
    is_admin: bool | None
    is_system_admin: bool | None
    disabled: bool | None
    created_at: datetime | None
    company_id: int | None
