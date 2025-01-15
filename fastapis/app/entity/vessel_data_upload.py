from datetime import datetime

from sqlmodel import Field, SQLModel


class VesselDataUpload(SQLModel, table=True):
    __tablename__ = "vessel_data_upload"

    id: int | None = Field(default=None, primary_key=True)

    file_path: str
    date_start: datetime | None
    date_end: datetime | None

    created_at: datetime = Field(default_factory=datetime.utcnow)

    vessel_id: int = Field(foreign_key="vessel.id")
