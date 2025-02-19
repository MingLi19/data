import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.entity.company import Company


@pytest.fixture(name="setup")
def setup(session: Session):
    test_company = Company(
        id=1,
        name="Company Test",
    )
    session.add(test_company)
    session.commit()
    session.close()


def test_read_companies(client: TestClient, setup: None):
    response = client.get("/company/").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data.__len__() == 1


def test_read_company(client: TestClient, setup: None):
    response = client.get("/company/1").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "Company Test"


def test_read_company_not_found(client: TestClient):
    response = client.get("/company/2")
    assert response.status_code == 404
    assert response.json()["message"] == "公司不存在"


def test_create_company(client: TestClient):
    response = client.post(
        "/company/",
        json={
            "name": "Company A",
        },
    ).json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "Company A"


def test_create_company_duplicate(client: TestClient, setup: None):
    response = client.post(
        "/company/",
        json={
            "name": "Company Test",
        },
    ).json()
    code = response["code"]
    assert code == 400


def test_update_company(client: TestClient, setup: None):
    response = client.put(
        "/company/1",
        json={
            "name": "Company B",
        },
    ).json()
    print(response)
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "Company B"


def test_delete_company(client: TestClient, setup: None):
    response = client.delete("/company/1").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "Company Test"

    not_found_response = client.get("/company/1")
    assert not_found_response.status_code == 404
    assert not_found_response.json()["message"] == "公司不存在"
