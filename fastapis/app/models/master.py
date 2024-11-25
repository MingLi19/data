from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class ShipTypeInsert(BaseModel):
    name_cn: str
    name_en: str
    code: str


# Data Model -> Master Data -> Ship Type
class ShipType(SQLModel, table=True):
    __tablename__ = "ship_type"
    id: int = Field(primary_key=True)
    name_cn: str
    name_en: str
    code: str
