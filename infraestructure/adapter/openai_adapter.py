import openai
import logging

from domain.port.openai_port import OpenAIPort
from infraestructure.adapter.config import Config
from dotenv import load_dotenv


load_dotenv()
config = Config()


class OpenAIAdapter:
    """
    This is a class for OpenAIAdapter.

    """

    def __init__(self):
        self.respuesta = {}

    def ask_openai(self, question: str, text: str, task: str):
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
            engine=config["engine"],
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
