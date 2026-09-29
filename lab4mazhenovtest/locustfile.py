from locust import HttpUser, task, between
import random
import string

def random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + "@test.com"

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def get_users(self):
        self.client.get("/api/users")

    @task(1)
    def create_user(self):
        payload = {
            "name": "user_" + ''.join(random.choices(string.ascii_lowercase, k=5)),
            "email": random_email()
        }
        self.client.post("/api/users", json=payload)