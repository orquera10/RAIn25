# Django

## Creación de un proyecto

Clonar un repositorio

Crear entorno virtual

Instalar dependencias

Crear un proyecto:

    django-admin startproject config .

Ejecutar el servidor:

    python manage.py runserver

Cambiar el idioma en config/settings.py

    LANGUAGE_CODE = 'es'

Crear aplicación

    python manage.py startapp core

Después hay que registrarla en settings

Crear migraciones

    python manage.py makemigrations

    python manage.py migrate

Crear superusuario

    python manage.py createsuperuser