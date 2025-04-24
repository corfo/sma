import requests
import json
from funciones import log
from os import environ
from dotenv import load_dotenv
load_dotenv()


url=f"{environ.get("RENDER_URL")}/api/all/"
headers = {"Authorization": f"Bearer {environ.get("mtt_user_TOKEN")}"}
log(url)
response = requests.get(url, headers=headers)
log(f"\n{json.dumps(response.json(), indent=4)}")

