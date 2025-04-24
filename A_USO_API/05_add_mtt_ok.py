import requests
from funciones import log, eliminarRegistros
import random
from os import environ
from dotenv import load_dotenv
load_dotenv()

eliminarRegistros('MTT', environ.get("mtt_user_TOKEN"))
#######
url=f"{environ.get("RENDER_URL")}/api/add/"
headers = {"Authorization": f"Bearer {environ.get("mtt_user_TOKEN")}"}

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