from django.test import TestCase, Client

# Test del endpoint ping
class HealthyTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_healthy_get(self):
        response = self.client.get('/api/healthy/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"message": "Estoy aqui"})

    def test_healthy_post(self):
        response = self.client.post('/api/healthy/')
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content, {"message": "Estoy aqui"})

class AllTests(TestCase):
    def setUp(self):
        self.client= Client()
    def test_AllFail(self):
        response =self.client.get('/api/all/')
        self.assertEqual(response.status_code,401)