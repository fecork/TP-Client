import requests
from tenacity import Retrying

from app.domine.port.cognitve_search_port import CognitiveSearchPort
from app.domine.modelo.arrendatario_dto import ArrendatarioDto
from app.domine.service.validar_fechas import ValidarFechas
from dotenv import load_dotenv
from fastapi.logger import logger

load_dotenv()


# class CognitiveSearchAdapter(portMysql):
class CognitiveSearchAdapter:
    def __init__(self):
        self.respuesta = {}

    def query_cognitive_search(self, question) -> dict:
        logger.warning(__name__)

        return {question: "respuesta"}

        # # Reemplaza estos valores con los tuyos
        # service_name = "cognitivesearchstoryfai"
        # api_key = "xLYqQeCoCPpiaqYTsoZFYnFAApOCuZHuczw7kLIMx7AzSeCZuK7I"
        # index_name = "tpclient-index"

        # # Define los parámetros de la consulta
        # params = {
        #     "api-version": "2021-04-30-Preview",
        #     "search": question,
        #     "queryLanguage": "es-ES",
        #     "speller": "lexicon",
        #     "queryType": "semantic",
        #     "captions": "extractive",
        #     "answers": "extractive|count-3",
        #     "semanticConfiguration": "tpclientconf",
        # }

        # # Construye la URL del servicio
        # url = f"https://{service_name}.search.windows.net/indexes/{index_name}/docs"

        # # Define el encabezado con la clave de API
        # headers = {"api-key": api_key}

        # # Hace el request y obtiene la respuesta
        # response = requests.get(url, params=params, headers=headers)

        # # Imprime el resultado
        # result = response.json()
        # # print(result["value"])
        # value = result["value"]
        # document = result["value"][0]["metadata_storage_path"]
        # # list_documents = [value[0]["metadata_storage_path"],value[1]["metadata_storage_path"]]
        # list_documents = []
        # len_value = len(value) - 1

        # for i in range(len(value)):
        #     doc = value[i]["metadata_storage_path"]
        #     list_documents.append(doc)

        # list_desencript = []
        # for documents in list_documents:
        #     list_desencript.append(desencriptar(str(document)))
        # answers = result["@search.answers"]

        # if len(answers) != 0:
        #     list_texts = []
        #     for answer in answers:
        #         list_texts.append(answer["text"])
        #         highlights = answer["highlights"]

        #     text = "\n".join(list_texts)
        #     return {"text": text, "document": str(list_desencript)}
        # else:
        #     text = result["value"][0]["content"]
        #     return {"text": text, "document": str(list_desencript)}
