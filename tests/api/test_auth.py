password = "AdminIsCool123!"

def test_successful_register_and_login(client):
    response = client.post(
        "/auth/register",
        json={"email": "rick89@gmail.com", "password": password}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "rick89@gmail.com"

    response = client.post(
        "/auth/login",
        data={"username": "rick89@gmail.com", "password": password}
    )
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"


def test_register_existing_email(client):
    response = client.post(
        "/auth/register",
        json={"email": "rick89@gmail.com", "password": password}
    )

    assert response.status_code == 400


def test_login_invalid_credentials(client):
    response = client.post(
        "/auth/login",
        data={"username": "invalid@gmail.com", "password": "faulty"}
    )

    assert response.status_code == 401


