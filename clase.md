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

Clase 2 Febrero

Para inicializar
    python -m  venv .venv
    .venv\Scripts\activate
    pip install django

Para no instalar varios paquetes, se puede crear un archivo config
    config install django
    pip freeze > requirements.txt (Entrega que paquetes se tiene instalados en .venv)
    pip install -r requirements.txt (Para instalar los requerimientos)

Apenas se crea una aplicacion, se debe registrarla en settings
INSTALLED APPS
Para instalarla
    cd src
    python manage.py 

En core se creo una funcion que responde con HTML
Para verlo
    python manage.py runserver

Se va a crear otra url
En el archivo views.py
    def saludar_con_etiqueta(request):
        return HttpResponse('<h1>Este es el titulo de mi App</h1>')

Luego en el archivo urls se agrega ultimo
    path('saludar_con_etiqueta/', views.saludar_con_etiqueta)

Creando el primer Template (plantilla)
1Dentro de la aplicacion se crea una carpeta llamada templates, en la miosma, otra que se llame igual a la aplicacion
2Dentro de esa carpeta sse crea uun archivo index.html
3Dentro de index.html se apreta ! para crear el body
4Dentro de body se escribe lo que queresmos qque se vea en la pagina
5Se agrega una funcion en core/views.py
6Se va a config/settings.urls y se crea una URL, que cuando el usuario solicite (request) tal URL, la funcion controladora index, responda la pagina index

Bases de datos relacionales

