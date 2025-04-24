import requests
import json
import sys
import os
ruta_token = os.path.abspath(".venv")
sys.path.append(ruta_token)
import token_users as t
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(m):
    logging.info(f"{m}")
def err(m):
    logging.error(f"{m}")

#####
def eliminarRegistro(data, user_token):
    url=f"{t.url}/api/delete/"
    headers = {"Authorization": f"Bearer {user_token}"}
    response = requests.post(url, headers=headers, json=data)
    log(f"DELETE StatusCode {response.status_code}")

def eliminarRegistros(organismo, user_token):
    url=f"{t.url}/api/all/"
    headers = {"Authorization": f"Bearer {user_token}"}
    data = requests.get(url, headers=headers).json()

    lista=[]
    for ppda in data:
        for medida in ppda.get('medidas',[]):
            if medida.get('organismo','')==organismo:
                log(medida.get('nombre'))
                for registro in medida.get('registros',[]):
                    tmp={'ppda': ppda.get('nombre'), 'medida':medida.get('nombre'), 'fecha':registro.get('fecha')}
                    lista.append(tmp)
    unicos = []
    vistos = set()
    for item in lista:
        clave = json.dumps(item, sort_keys=True)
        if clave not in vistos:
            vistos.add(clave)
            unicos.append(item)
    for registro in unicos:
        eliminarRegistro(registro,user_token)
