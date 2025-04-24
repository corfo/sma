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

def getData(ppda):
    return {
        "ppda" : ppda,
        "medida": "CHARLAS DE PREVENCION",
        "fecha": "2025-02-21",
        "indicadores": [
            { "nombre": "CHARLAS PROGRAMADAS", "valor": random.randint(1, 100)},
            { "nombre": "CHARLAS REALIZADAS", "valor": random.randint(1, 100)},
            ]
    }

ppda = "PPDA QUINTERO"
add(getData(ppda))

ppda = "PPDA ARICA"
add(getData(ppda))