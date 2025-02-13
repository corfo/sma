# DB
```
docker run -d --restart always --name postgres_sma -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=Amdni842 -e POSTGRES_DB=sma -p 55432:5432 postgres:latest
```

# vevn Windows
## Crear venv
```
python -m venv venv
```
## Activar venv
```
venv\Scripts\activate
```

## Instalar Librerias
```
pip install -r requirements.txt
```

# Crear el proyecto y app en django
```
django-admin startproject poject_sma .
python manage.py startapp app_ppda
```

# crear superuser
```
python manage.py createsuperuser --username admin
```
email: admin@sma.cl  
password: admin123  
