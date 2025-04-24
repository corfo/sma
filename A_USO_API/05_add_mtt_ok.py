import requests
import json
import sys
import os
from funciones import log, err, eliminarRegistros
ruta_token = os.path.abspath(".venv")
sys.path.append(ruta_token)
import token_users as t
import random
eliminarRegistros('MTT', t.mtt_user_token)
#######
url=f"{t.url}/api/add/"
headers = {"Authorization": f"Bearer {t.mtt_user_token}"}

def add(data):
    response = requests.post(url, headers=headers, json=data)
    log(f"StatusCode {response.status_code} {response.text}")

log("   ---   1- ADD OK   ---")
data = {
    "ppda" : "PPDA QUINTERO",
    "medida": "BUSES CONTAMINANTES",
    "fecha": "2025-02-10",
    "indicadores": [
        { "nombre": "BUSES INSCRITOS", "valor": random.randint(1, 100)},
        { "nombre": "BUSES CONTAMINANTES", "valor": random.randint(1, 100)},
        ]
    }
add(data)

log("   ---   2- ADD FALLA   ---")
add(data)

log("   ---   3- ADD FALLA  ---")
data = {
    "ppda" : "PPDA QUINTERO",
    "medida": "BUSES CONTAMINANTES",
    "fecha": "2025-02-11",
    "indicadores": [
        { "nombre": "BUSES INSCRITOS", "valor": random.randint(1, 100)},
        ]
    }
add(data)

log("   ---   4- ADD FALLA  ---")
data = {
    "ppda" : "PPDA QUINTERO",
    "medida": "BUSES CONTAMINANTES",
    "fecha": "2025-02-12",
    "indicadores": [
        { "nombre": "BUSES INSCRITOS", "valor": random.randint(1, 100)},
        { "nombre": "BUSES CONTAMINANTES", "valor": random.randint(1, 100)},
        { "nombre": "BUSES CONTAMINANTES", "valor": random.randint(1, 100)},
        ]
    }
add(data)

log("   ---   5- ADD FALLA  ---")
data = {
    "ppda" : "PPDA QUINTERO",
    "medida": "BUSES CONTAMINANTES",
    "fecha": "2025-02-13",
    "indicadores": [
        { "nombre": "BUSES INSCRITOS", "valor": random.randint(1, 100)},
        { "nombre": "BUSES CONTAMINANTES", "valor": random.randint(1, 100)},
        { "nombre": "BUSES xxxxxxxxxxxx", "valor": random.randint(1, 100)},
        ]
    }
add(data)