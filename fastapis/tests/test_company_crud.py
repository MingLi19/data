from fastapi.testclient import TestClient


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
