import requests
import json
from funciones import log
import random
from os import environ
from dotenv import load_dotenv
load_dotenv()

#######################
url=f"{environ.get("RENDER_URL")}/api/add/"
headers = {"Authorization": f"Bearer {environ.get("mtt_user_TOKEN")}"}
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