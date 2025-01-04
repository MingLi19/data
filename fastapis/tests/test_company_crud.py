import pytest
from app.models.company import Company
from fastapi.testclient import TestClient
from sqlmodel import Session


@pytest.fixture(name="setup")
def setup(session: Session):
    test_company = Company(
        id=1,
        name="Company Test",
        address="Address Test",
        contact_person="John Doe",
        contact_phone="12345678",
        contact_email="test@163.com",
    )
    session.add(test_company)
    session.commit()
    session.close()


def test_read_company(client: TestClient, setup: None):
    response = client.get("/company/1").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "Company Test"


def test_create_company(client: TestClient):
    response = client.post(
        "/company/",
        json={
            "name": "Company A",
            "address": "123 Main St, New York, NY",
            "contact_person": "John Doe",
            "contact_phone": "12345678",
            "contact_email": "test@163.com",
        },
    ).json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "Company A"


def test_update_company(client: TestClient, setup: None):
    response = client.put(
        "/company/1",
        json={
            "name": "Company B",
            "address": "123 Main St, New York, NY",
            "contact_person": "John Doe",
            "contact_phone": "12345678",
            "contact_email": "test@163.com",
        },
    ).json()
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
