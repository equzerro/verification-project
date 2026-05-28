import requests
import time


def test_api_response_time():
    start = time.time()

    response = requests.post(
        "http://localhost:8000/login",
        json={
            "username": "admin",
            "password": "admin123",
            "email": "admin@test.com"
        }
    )

    elapsed = time.time() - start

    assert response.status_code == 200
    assert elapsed < 0.5