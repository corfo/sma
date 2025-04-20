from django.test import TestCase, Client
from datetime import datetime
from unittest.mock import patch

# Test del endpoint ping
class HealthyTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_healthy_get(self):
        fecha_esperada="2025-04-20T12:00:00"
        with patch("app_ppda.views.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime.fromisoformat(fecha_esperada)
            response = self.client.get('/api/healthy/')
            self.assertEqual(response.status_code, 200)
            self.assertJSONEqual(response.content, {"message": "Estoy aqui", "date": fecha_esperada})

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