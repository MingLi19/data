import pytest
from sqlmodel import Session

from app.entity.company import Company
from app.entity.user import User


@pytest.fixture(name="setup")
def setup(session: Session):
    test_user = User(
        id=1,
        name="User Test",
        username="user_test",
        hashed_password="123456",
        phone="12345678999",
        company=Company(id=1, name="Company Test"),
    )
    session.add(test_user)
    session.commit()
    session.close()


def test_read_users(client, setup):
    response = client.get("/user/").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data.__len__() == 1


def test_read_user(client, setup):
    response = client.get("/user/1").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "User Test"


def test_create_user(client):
    response = client.post(
        "/user/",
        json={
            "name": "User A",
            "username": "user_a",
            "hashed_password": "123456",
            "phone": "12345678999",
            "company_id": 1,
        },
    ).json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "User A"


def test_update_user(client, setup):
    response = client.put(
        "/user/1",
        json={
            "name": "User B",
            "username": "user_b",
            "hashed_password": "123456",
            "phone": "12345678999",
            "company_id": 1,
        },
    ).json()
    print(response)
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "User B"


def test_delete_user(client, setup):
    response = client.delete("/user/1").json()
    code = response["code"]
    data = response["data"]
    assert code == 200
    assert data["name"] == "User Test"

    not_found_response = client.get("/user/1")
    assert not_found_response.status_code == 404
    assert not_found_response.json()["detail"] == "用户不存在"
