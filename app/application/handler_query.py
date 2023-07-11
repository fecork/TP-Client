from fastapi.logger import logger
from app.domine.service.search_cognitive import SearchCognitive
from app.domine.excepciones.error_del_negocio import ErrorDelNegocio
from app.infraestructure.adaptador.cognitive_search_adapter import (
    CognitiveSearchAdapter,
)


query = SearchCognitive()
adaptador = CognitiveSearchAdapter()
error_del_negocio = ErrorDelNegocio()


class HandlerQuery:
    def execute(self):
        """
        execute HandlerQuery
        """
        logger.warning(__name__)
        pregunta = "¿Cuánto debo pagar?"
        return query.execute_service(pregunta, adaptador)
        # return consultar.consultar_pagos(adaptador)
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
