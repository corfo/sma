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

usuario normal prueba pass Prue.,12389

# queries
```
select t1.nombre , t3.nombre , t5.nombre , t7.nombre , t6.periodo , t6.valor  from app_ppda_ppda t1  
inner join app_ppda_ppdaorganismo t2 on t1.id = t2.ppda_id  
inner join app_ppda_organismo t3 on t2.organismo_id = t3.id  
inner join app_ppda_ppdaorganismo_medidas t4 on t4.ppdaorganismo_id =t2.id  
inner join app_ppda_medida t5 on t5.id = t4.medida_id  
inner join app_ppda_medidaindicador t6 on t6.medida_id = t5.id  
inner join app_ppda_indicador t7 on t7.id = t6.indicador_id  
```

# Usuarios

seguridad
transporte

pass Password.123

# Ejecucion en distintos entornos

## POSTGRES ONLINE
```
python manage.py migrate --setting=poject_sma.settings_pro
```

## POSTGRES LOCAL
```
python manage.py migrate --setting=poject_sma.settings_dev
```

## SQLITE
```
python manage.py migrate --setting=poject_sma.settings_test
```