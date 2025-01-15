import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.entity.company import Company
from app.entity.meta import ShipType, TimeZone
from app.entity.vessel import Vessel
from app.entity.vessel_data_upload import VesselDataUpload


@pytest.fixture(name="setup")
def setup(session: Session):
    test_company = Company(
        id=1,
        name="Company Test",
    )
    session.add(test_company)
    test_ship_type = ShipType(
        id=1,
        name_cn="散货船",
        name_en="Bulk carrier",
        code="I001",
    )
    session.add(test_ship_type)
    test_time_zone = TimeZone(
        id=1,
        name_cn="中国标准时间",
        name_en="China Standard Time",
        explaination="UTC+8",
    )
    session.add(test_time_zone)
    test_vessel = Vessel(
        id=1,
        name="船名",
        mmsi="1",
        build_date="2024-12-06",
        gross_tone=1.0,
        dead_weight=2.0,
        new_vessel=True,
        hull_clean_date="2024-12-06",
        engine_overhaul_date="2024-12-06",
        newly_paint_date="2024-12-06",
        propeller_polish_date="2024-12-06",
        company_id=1,
        equipments=[],
        ship_type_id=1,
        time_zone_id=1,
    )
    session.add(test_vessel)
    test_upload_record = VesselDataUpload(
        id=1,
        vessel_id=1,
        file_path="upload/2021-02-01/data.csv",
    )
    session.add(test_upload_record)
    session.commit()
    session.close()


def test_read_vessel_data_upload_history(client: TestClient, setup: None):
    response = client.get("/upload/vessel/1/history").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data.__len__() == 1
    assert data[0]["file_path"] == "upload/2021-02-01/data.csv"


def test_upload_orginal_zip(client: TestClient, setup: None):
    response = client.post("/upload/vessel/1/original", files={"file": ("data.csv", b"filecontent")})
    code = response.json()["code"]
    assert code == 200
    assert response.json()["message"] == "上传成功"
