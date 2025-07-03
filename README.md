#1   instalar python

#2 pip install django

#3 pip install psycopg2-binary

#4 modificar la bd con tus datos en settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alquiler',#nombre de tu base de datos
        'USER': 'postgres',
        'PASSWORD': 'root',#contraseña
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

terminal del proyecto
#5 python manage.py makemigrations
python manage.py migrate

#6 python manage.py runserver

#7 http://127.0.0.1:8000/usuarios/
http://127.0.0.1:8000/registros/
http://127.0.0.1:8000/cuartos/
http://127.0.0.1:8000/departamentos/
