import requests
from os import environ
from funciones import log, err, actualizarEnvConToken
from dotenv import load_dotenv
load_dotenv()

def getToken(userx,passx):
    data = {
        'username': userx,
        'password': passx
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        tokens = response.json()
        with open(archivo, "a") as file:
            #file.write(f"{userx}_token='{tokens['access']}'\n")
            actualizarEnvConToken(userx,tokens['access'])
        log(f"Token para {userx} generado")
    else:
        err("Error:", response.status_code)
        err(response.text)

####
url = f"{environ.get("RENDER_URL")}/api/token/"
archivo='.venv/token_users.py'
#with open(archivo, "w") as file:
#    file.write(f"url='{environ.get("RENDER_URL")}'\n")
getToken(environ.get('conaf_user'), environ.get('conaf_pass'))
getToken(environ.get('mtt_user'),   environ.get('mtt_pass'))