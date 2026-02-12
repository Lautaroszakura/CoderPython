#El primer commit se hace de forma automatica

#Se creara un entorno virtual con Django
-Para crear el entorno virtual, se abre la terminal

    python -m venv .venv

-Para activar el entorno virtual

    .\.venv\Scripts\activate
    #(.venv) Se activa el entorno virtual al lado de la consola

-Se crea un nuevo archivo

    .gitignore
    #Se introduce .venv para ignorar el entorno virtual

-Django
Es un framework de desarrollo web de codigo abierto escrito en python que permite construir aplicaciones web de forma rapida y eficiente
Proporciona una estructura y conjnto de herramientas para simplificar el proceso de creacion de aplicaciones web, lo que permite a los desarrolladores centrarse en la logica de la palicacion en lugar de preocuparse por la configuracion de la estructura

    #Se debe tener el entorno virtual activado
    pip install django

-Pasos para crear proyecto

1En VS, dentro de la carpeta que acaba de crear git clone e instalado Django

2Crea una carpeta llamada src yu luego ingresa a la carpeta y ejecuta djang-admin para crear la estructura de configuracion de proyecto Django

    cd src

    django-admin startproject config .
    #Se creara la carpeta config dentro de src

3Se ejecutara el servidor Django mediante manage.py
 Dentro de src, se ejecuta en la terminal

    python manage.py runserver #Se inicializa el servidor de Django
    #Ctrl+C para poder escribir
    #Se hacen los commit para todo
    #Se hace git push para subirlo a la nube

Creacion de aplicacion Django

    python manage.py startapp core
    #Se hace un commit
    #Se agrega core a las app instaladas en settings, y se hace el commit

Primera vista
    Dentro de la carpeta core
    Ir a vista y agregar la importacion

        from django.http import HttpResponse