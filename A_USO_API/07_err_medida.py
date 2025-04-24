import requests
import json
import sys
import os
from funciones import log, err, eliminarRegistros
ruta_token = os.path.abspath(".venv")
sys.path.append(ruta_token)
import token_users as t
import random
#######
url=f"{t.url}/api/add/"
headers = {"Authorization": f"Bearer {t.conaf_user_token}"}

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