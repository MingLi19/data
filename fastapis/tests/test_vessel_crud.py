import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.entity.company import Company
from app.entity.meta import ShipType, TimeZone
from app.entity.vessel import Vessel


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
    session.commit()
    session.close()


def test_read_vessels(client: TestClient, setup):
    response = client.get("/vessel").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data.__len__() == 1


def test_read_vessel(client: TestClient, setup):
    response = client.get("/vessel/1").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "船名"


def test_read_vessel_not_found(client: TestClient):
    response = client.get("/vessel/2")
    assert response.status_code == 404
    assert response.json()["message"] == "船舶不存在"


def test_create_vessel(client: TestClient, setup):
    response = client.post(
        "/vessel/",
        json={
            "name": "船名A",
            "mmsi": "2",
            "build_date": "2024-12-06",
            "gross_tone": 1.0,
            "dead_weight": 2.0,
            "new_vessel": True,
            "hull_clean_date": "2024-12-06",
            "engine_overhaul_date": "2024-12-06",
            "newly_paint_date": "2024-12-06",
            "propeller_polish_date": "2024-12-06",
            "company_id": 1,
            "ship_type_id": 1,
            "time_zone_id": 1,
            "equipments": [
                {
                    "name": "发动机",
                    "type": "me",
                    "fuel_type_ids": [1, 2],
                },
                {
                    "name": "柴油发电机",
                    "type": "dg",
                },
                {
                    "name": "锅炉",
                    "type": "blr",
                },
            ],
            "power_speed_curve": [
                {
                    "power": 1000,
                    "speed": 10,
                },
                {
                    "power": 2000,
                    "speed": 20,
                },
            ],
        },
    ).json()
    code = response["code"]
    vessel = response["data"]
    assert code == 200
    assert vessel["name"] == "船名A"
    assert vessel["equipments"].__len__() == 3


def test_update_vessel(client: TestClient, setup):
    response = client.put(
        "/vessel/1",
        json={
            "name": "船名B",
            "mmsi": "123456789",
            "build_date": "2024-12-06",
            "gross_tone": 1.0,
            "dead_weight": 2.0,
            "new_vessel": True,
            "hull_clean_date": "2024-12-06",
            "engine_overhaul_date": "2024-12-06",
            "newly_paint_date": "2024-12-06",
            "propeller_polish_date": "2024-12-06",
            "company_id": 1,
            "ship_type_id": 1,
            "time_zone_id": 1,
            "equipments": [
                {
                    "name": "新发动机",
                    "type": "me",
                    "fuel_type_ids": [1, 2],
                },
            ],
        },
    ).json()
    code = response["code"]
    vessel = response["data"]
    print("vessel: ", vessel)
    assert code == 200
    assert vessel["name"] == "船名B"
    assert vessel["equipments"].__len__() == 1
    assert vessel["equipments"][0]["name"] == "新发动机"


def test_delete_vessel(client: TestClient, setup):
    response = client.delete("/vessel/1").json()
    code = response["code"]
    message = response["message"]
    assert code == 200
    assert message == "船舶删除成功"

    not_found_response = client.get("/vessel/1")
    assert not_found_response.status_code == 404
    assert not_found_response.json()["message"] == "船舶不存在"
