import requests
import json
from funciones import log, eliminarRegistros
import random
from os import environ
from dotenv import load_dotenv
load_dotenv()

eliminarRegistros('CONAF', environ.get("conaf_user_TOKEN"))
##########################
url=f"{environ.get("RENDER_URL")}/api/add/"
headers = {"Authorization": f"Bearer {environ.get("conaf_user_TOKEN")}"}
data = {
    "ppda" : "PPDA QUINTERO",
    "medida": "CORTA FUEGOS",
    "fecha": "2025-01-01",
    "indicadores": [
        { "nombre": "METROS CONSTRUIDOS", "valor": random.randint(1, 100)},
        ]
    }
log(url)
response = requests.post(url, headers=headers, json=data)
log(f"StatusCode {response.status_code}")
log(f"\n{json.dumps(response.json(), indent=4)}")