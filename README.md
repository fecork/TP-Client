# API to search in Cognitive Search and GPT - TP Client

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

    git clone https://fecork@bitbucket.org/fecork/tp_client_cognitiveservicespy.git

### Pre-requisitos 📋

    Python > 3.8
    Pipenv
    OpenAI
    Requests
    FastAPI
    uvicorn
    dotenv

### Instalación 🔧

Pipenv es un manejador de dependencias para los proyectos de Python,
para instalar
Install:

    pip install --user pipenv

Instalamos las librerías del proyecto

    pipenv install --dev

# VARIABLES DE ENTORNO

se necesita configurar las siguientes variables de entorno, en el respectivo archivo ´.env´

    CS_SERVICE_NAME= Cognitive Search Name
    CS_API_KEY= Cognitive Search Key
    CS_INDEX_NAME="Cognitive Search Index

    OPENAI_API_KEY= Open AI Key
    OPENAI_API_BASE= Open AI URL
    OPENAI_API_TYPE= Open AI Type (Azure, OpenAI)
    OPENAI_API_VERSION=Open AI Version

# DATABASE

Iniciamos el entorno de trabajo:

    pipenv shell

ejecutamos

    pipenv run python setup_db.py

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

podemos realizar todas las pruebas

    pytest tests/

especificar una capa de la arquitectura hexagonal

    pytest tests/adapters/test_open_ai_adapter.py

especificar un test

    pytest tests/adapters/test_open_ai_adapter.py -k test_login_openai

# REST

Iniciamos el entorno de trabajo:

    pipenv shell

Iniciamos el service en el port 3000, en modo desarrollador:

    uvicorn main:app --port 3000 --reload

para ver la documentación de la API podemos ingresar a
http://localhost:8084/docs.

# TEST

Para ejecutar el test, con el entorno de trabajo activado (`pipenv shell`):

    pytest

# DOC

para ver la documentación de la API podemos ingresar a

### swagger

[http://localhost:8084/docs](http://localhost:8084/docs)

### documentación alternativa

[http://localhost:8084/redoc](http://localhost:8084/redoc)

## Despliegue 📦

para desplegar FastAPI en Azure App Service en configurar los archivos startup.sh y gunicorn.py,
mas información en
[Wiki](https://fecork.notion.site/Desplegar-un-servicio-con-FastAPI-en-Azure-App-Service-b9b6a4be99bc4c1882e1acc5a9870bd8?pvs=4)

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

- [OpenAI]() - Modelo GPT
- [Cognitive Search]() - Indexador de datos
- [Fast API]() - El framework web usado

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

- **Wilberth Ferney Córdoba Canchala** - _Trabajo Inicial_ - [LinkenId]()

## Expresiones de Gratitud 🎁

- Comenta a otros sobre este proyecto 📢
- Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
- Da las gracias públicamente 🤓.
- etc.
