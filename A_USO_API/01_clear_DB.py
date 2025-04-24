from funciones import eliminarRegistros
from os import environ
from dotenv import load_dotenv
load_dotenv()

eliminarRegistros('MTT',environ.get("mtt_user_TOKEN"))
eliminarRegistros('CONAF',environ.get("conaf_user_TOKEN"))
