from utils.api_client import post

def test_login_success():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = post("/api/login", payload)

    assert response.status_code == 200
    assert "token" in response.json()


def test_login_failure_missing_password():
    payload = {
        "email": "eve.holt@reqres.in"
    }
    response = post("/api/login", payload)

    assert response.status_code == 400
