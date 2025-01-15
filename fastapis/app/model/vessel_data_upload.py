from datetime import date

from pydantic import BaseModel


class VesselDataUploadBase(BaseModel):
    file_path: str
    date_start: date | None = None
    date_end: date | None = None


class VesselDataUploadCreate(VesselDataUploadBase):
    pass

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "file_path": "upload/2021-02-01/data.csv",
                    "date_start": "2025-01-01",
                    "date_end": "2025-01-31",
                }
            ]
        }
    }
