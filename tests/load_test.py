from locust import HttpUser, task


class WebsiteUser(HttpUser):

    @task
    def login(self):
        self.client.post(
            "/login",
            json={
                "username": "admin",
                "password": "admin123",
                "email": "admin@test.com"
            }
        )