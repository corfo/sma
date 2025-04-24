import os, sys
from funciones import eliminarRegistros
ruta_token = os.path.abspath(".venv")
sys.path.append(ruta_token)
import token_users as t

eliminarRegistros('MTT',t.mtt_user_token)
eliminarRegistros('CONAF',t.conaf_user_token)
