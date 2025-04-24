import requests
import json
import sys
import os
from funciones import log, err
ruta_token = os.path.abspath(".venv")
sys.path.append(ruta_token)
import token_users as t

url=f"{t.url}/api/all/"
headers = {"Authorization": f"Bearer {t.mtt_user_token}"}
log(url)
response = requests.get(url, headers=headers)
log(f"\n{json.dumps(response.json(), indent=4)}")

