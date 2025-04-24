import requests
import json
import sys
import os
from funciones import log, err, eliminarRegistros
ruta_token = os.path.abspath(".venv")
sys.path.append(ruta_token)
import token_users as t
import random
#######################
url=f"{t.url}/api/add/"
headers = {"Authorization": f"Bearer {t.mtt_user_token}"}
data = {
    "ppda" : "PPDA QUINTERO",
    "medida": "CORTA FUEGOS",
    "fecha": "2025-02-02",
    "indicadores": [
        { "nombre": "METROS CONSTRUIDOS", "valor": random.randint(1, 100)},
        ]
    }
log(url)
response = requests.post(url, headers=headers, json=data)
log(f"StatusCode {response.status_code}")
log(f"\n{json.dumps(response.json(), indent=4)}")