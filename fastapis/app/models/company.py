from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class CompanyBase(SQLModel):
    name: str = Field(unique=True, nullable=False)
    address: str | None
    contact_person: str | None
    contact_phone: str | None
    contact_email: str | None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Company A",
                    "address": "123 Main St, New York, NY",
                    "contact_person": "John Doe",
                    "contact_phone": "12345678",
                    "contact_email": "test@163.com",
                }
            ]
        }
    }


class Company(CompanyBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CompanyCreate(CompanyBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Company A",
                    "address": "123 Main St, New York, NY",
                    "contact_person": "John Doe",
                    "contact_phone": "12345678",
                    "contact_email": "test@163.com",
                }
            ]
        }
    }


class CompanyUpdate(BaseModel):
    name: str | None
    address: str | None
    contact_person: str | None
    contact_phone: str | None
    contact_email: str | None
