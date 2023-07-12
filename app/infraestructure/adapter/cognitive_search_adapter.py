import requests
from tenacity import Retrying

from app.domine.port.cognitve_search_port import CognitiveSearchPort
from app.domine.modelo.arrendatario_dto import ArrendatarioDto
from app.domine.service.validar_fechas import ValidarFechas
from dotenv import load_dotenv
from fastapi.logger import logger

load_dotenv()


class CognitiveSearchAdapter:
    def __init__(self):
        self.respuesta = {}

    def query_cognitive_search(self, question) -> dict:
        logger.warning(__name__)

        return {question: "respuesta"}
