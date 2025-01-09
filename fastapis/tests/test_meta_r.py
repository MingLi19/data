import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.entity.meta import FuelType, ShipType, TimeZone


@pytest.fixture(name="setup")
def setup(session: Session):
    test_fuel_type = FuelType(
        id=1,
        name_cn="液化天然气",
        name_en="Liquefied Natural Gas",
        name_abbr="LNG",
        cf=2.75,
    )
    test_ship_type = ShipType(
        id=1,
        name_cn="散货船",
        name_en="Bulk carrier",
        code="I001",
    )
    test_time_zone = TimeZone(
        id=1,
        name_cn="中国标准时间",
        name_en="China Standard Time",
        explaination="UTC+8",
    )
    session.add(test_fuel_type)
    session.add(test_ship_type)
    session.add(test_time_zone)
    session.commit()
    session.close()


def test_read_fuel_types(client: TestClient, setup: None):
    response = client.get("/meta/fuel_type").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data.__len__() == 1
    assert data[0]["name_cn"] == "液化天然气"


def test_read_ship_types(client: TestClient, setup: None):
    response = client.get("/meta/ship_type").json()
    print(response)
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data.__len__() == 1
    assert data[0]["name_cn"] == "散货船"


def test_read_time_zones(client: TestClient, setup: None):
    response = client.get("/meta/time_zone").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data.__len__() == 1
    assert data[0]["name_cn"] == "中国标准时间"
