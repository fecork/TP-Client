from fastapi.logger import logger
from app.domine.service.search_cognitive import SearchCognitive
from app.domine.excepciones.error_del_negocio import ErrorDelNegocio
from app.infraestructure.adapter.cognitive_search_adapter import (
    CognitiveSearchAdapter,
)

from app.domine.modelo.input_data_dto import InputDataDto

query = SearchCognitive()
adapter = CognitiveSearchAdapter()
error_del_negocio = ErrorDelNegocio()


class HandlerQuery:
    def execute(self, input_data):
        """
        execute HandlerQuery
        Args: input_data
        Returns: query.execute_service
        """
        logger.warning(__name__)
        logger.warning(f"input_data: {input_data}")
        pregunta = input_data["question"]
        return query.execute_service(pregunta, adapter)
        # return consultar.consultar_pagos(adapter)
        # cognitive_response = query_cognitive_search(question)
        # text_to_gpt = cognitive_response["text"]
        # indexed_document = cognitive_response["document"]

        # # text_to_gpt = summarizer(indexed_text)

        # gpt_response = ask_openai(question, text_to_gpt, "question")

        # print("====================")
        # print("buscamos el texto indexado: ")
        # print(cognitive_response)
        # print("====================")

        # print("RESPUESTA DE GPT-3")
        # print(f"de acuerdo a {indexed_document}")
        # print(gpt_response)
