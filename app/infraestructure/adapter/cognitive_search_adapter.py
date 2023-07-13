import requests
import os
import logging

from dotenv import load_dotenv
from app.domine.service.decrypt_64 import desencriptar
from app.domine.service.clean_text import clean_text
from app.infraestructure.adapter.config import Config


load_dotenv()
config = Config()


class CognitiveSearchAdapter:
    def __init__(self):
        self.respuesta = {}

    def query_cognitive_search(self, question) -> dict:
        logging.warning(__name__)
        service_name = os.environ.get("CS_SERVICE_NAME")
        api_key = os.environ.get("CS_API_KEY")
        index_name = os.environ.get("CS_INDEX_NAME")

        params = config.cognitive_search(question)

        url = f"https://{service_name}.search.windows.net/indexes/{index_name}/docs"

        headers = {"api-key": api_key}

        response = requests.get(url, params=params, headers=headers)

        result = response.json()
        value = result["value"]
        document = result["value"][0]["metadata_storage_path"]
        list_documents = []

        for i in range(len(value)):
            doc = value[i]["metadata_storage_path"]
            list_documents.append(doc)

        list_desencript = []
        for document in list_documents:
            list_desencript.append(desencriptar(str(document)))

        try:
            answers = result["@search.answers"]
            if len(answers) != 0:
                list_texts = []
                for answer in answers:
                    list_texts.append(answer["text"])
                    highlights = answer["highlights"]

                text = clean_text("\n".join(list_texts))
                return {"text": text, "document": str(list_desencript)}
            else:
                text = clean_text(result["value"][0]["content"])
                return {"text": text, "document": str(list_desencript)}

        except KeyError:
            answers = value[0]["merged_content"]
            if len(answers) != 0:
                return {
                    "text": clean_text(answers),
                    "document": str(list_desencript),
                }
            else:
                return {
                    "text": clean_text(answers),
                    "document": str(list_desencript),
                }
