import requests
from tenacity import Retrying

from app.domine.port.cognitve_search_port import CognitiveSearchPort
from app.domine.modelo.arrendatario_dto import ArrendatarioDto
from app.domine.service.validar_fechas import ValidarFechas
from dotenv import load_dotenv
from fastapi.logger import logger
import os
import openai
import logging
import numpy as np

load_dotenv()


class OpenAIAdapter:
    """
    This is a class for OpenAIAdapter.

    """

    def __init__(self):
        self.respuesta = {}

    def login_openai(self) -> dict:
        """
        This is a function for  login to openai.
        """
        logging.warning("Executing login_openai")
        try:
 

        except Exception as e:
            print("No credentials for openai")
            print(e)

    def ask_openai(self, question: str, text: str, task: str) -> dict:
        """
        This is a function for
        ask question to AZURE GPT by OpenAI.
        """
        logging.warning("Executing ask_openai")
        self.login_openai()
        prompt = """busca la información en el texto entregado entre ### ### y
                responde la pregunta de acuerdo al texto"""
        personality = "NOTA: explicaselo a un niño de 10 años"

        if task == "question":
            prompt = f"{prompt} {question} {personality}"
        if task == "summarizer":
            prompt = f"""haz un resumen con los aspectos mas importantes del texto,
                        de 100 palabras, TEXTO:{text}
                        """

        instrucciones = f"""
                            Tu papel es ayudar a responder preguntas del siguiente
                            texto.

                            ###
                            {text}
                            ###
                        """

        response = openai.ChatCompletion.create(
            engine="gpt-4-32k",  # engine = "deployment_name".
            messages=[
                {
                    "role": "system",
                    "content": instrucciones,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.7,
        )

        try:
            return (response["choices"][0]["message"]["content"].lstrip(),)

        except Exception as e:
            logging.warning("Error in ask_openai")
            logging.warning(e)
            logging.warning(response.choices)
