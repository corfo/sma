from django.test import TestCase, Client
from datetime import datetime
from unittest.mock import patch
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

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
            self.assertJSONEqual(response.content, {"message": "Estoy aqui y bien", "date": fecha_esperada})

    def test_healthy_post(self):
        response = self.client.post('/api/healthy/')
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content, {"message": "Estoy aqui"})

class AllTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = "testuser"
        self.password = "strongpassword123"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_AllFail(self):
        # Sin autenticación
        response = self.client.get('/api/all/')
        self.assertEqual(response.status_code, 401)

    def test_AllSuccess(self):
        # Obtener token JWT
        response = self.client.post('/api/token/', {
            "username": self.username,
            "password": self.password
        }, format="json")

        self.assertEqual(response.status_code, 200)

        # Extraer token de acceso
        token = response.data.get("access")
        self.assertIsNotNone(token)

        # Autenticar cliente con el token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        # Acceder al endpoint protegido
        response = self.client.get('/api/all/')
        self.assertEqual(response.status_code, 200)
