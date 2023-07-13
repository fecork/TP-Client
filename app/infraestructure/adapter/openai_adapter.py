import logging
import os
import openai
import logging

from app.domine.port.cognitve_search_port import CognitiveSearchPort
from app.infraestructure.adapter.config import Config
from dotenv import load_dotenv


load_dotenv()
config = Config()


class OpenAIAdapter:
    """
    This is a class for OpenAIAdapter.

    """

    def __init__(self):
        self.respuesta = {}

    def ask_openai(self, question: str, text: str, task: str) -> dict:
        """
        This is a function for
        ask question to AZURE GPT by OpenAI.
        """
        logging.warning("Executing ask_openai")
        config = Config().openai(text)

        prompt = config["prompt"]
        personality = config["personality"]

        if task == "question":
            prompt = f"{prompt} {question} {personality}"
        if task == "summarizer":
            prompt = f"""haz un resumen con los aspectos mas importantes del texto,
                        de 100 palabras, TEXTO:{text}
                        """

        instrucciones = config["instrucciones"]

        response = openai.ChatCompletion.create(
            engine=config["engine"],  # engine = "deployment_name".
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
            temperature=config["temperature"],
        )

        try:
            return response["choices"][0]["message"]["content"].lstrip()

        except Exception as e:
            logging.warning("Error in ask_openai")
            logging.warning(e)
            logging.warning(response.choices)