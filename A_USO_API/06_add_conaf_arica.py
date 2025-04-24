import requests
from funciones import log
import random
from os import environ
from dotenv import load_dotenv
load_dotenv()

#######
url=f"{environ.get("RENDER_URL")}/api/add/"
headers = {"Authorization": f"Bearer {environ.get("conaf_user_TOKEN")}"}

def add(data):
    response = requests.post(url, headers=headers, json=data)
    log(f"StatusCode {response.status_code} {response.text}")

data = {
    "ppda" : "PPDA ARICA",
    "medida": "CHARLAS DE PREVENCION",
    "fecha": "2025-02-10",
    "indicadores": [
        { "nombre": "CHARLAS PROGRAMADAS", "valor": random.randint(1, 100)},
        { "nombre": "CHARLAS REALIZADAS", "valor": random.randint(1, 100)},
        ]
    }
add(data)

data = {
    "ppda" : "PPDA ARICA",
    "medida": "CHARLAS DE PREVENCION",
    "fecha": "2025-02-11",
    "indicadores": [
        { "nombre": "CHARLAS PROGRAMADAS", "valor": random.randint(1, 100)},
        { "nombre": "CHARLAS REALIZADAS", "valor": random.randint(1, 100)},
        ]
    }
add(data)

data = {
    "ppda" : "PPDA ARICA",
    "medida": "CHARLAS DE PREVENCION",
    "fecha": "2025-02-12",
    "indicadores": [
        { "nombre": "CHARLAS PROGRAMADAS", "valor": random.randint(1, 100)},
        { "nombre": "CHARLAS REALIZADAS", "valor": random.randint(1, 100)},
        ]
    }
add(data)

