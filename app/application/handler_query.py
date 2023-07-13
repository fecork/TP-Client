import logging
from app.domine.service.search_cognitive import SearchCognitive
from app.domine.service.clean_text import clean_text
from app.domine.excepciones.error_del_negocio import ErrorDelNegocio
from app.infraestructure.adapter.cognitive_search_adapter import (
    CognitiveSearchAdapter,
)
from app.infraestructure.adapter.openai_adapter import OpenAIAdapter

from app.domine.modelo.output_data_dto import OutputDataDto

query = SearchCognitive()
adapter_cs = CognitiveSearchAdapter()
adapter_gpt = OpenAIAdapter()
error_del_negocio = ErrorDelNegocio()


class HandlerQuery:
    def execute(self, input_data) -> OutputDataDto:
        """
        execute HandlerQuery
        Args: input_data
        Returns: query.execute_service
        """
        logging.warning(__name__)
        logging.warning(f"input_data: {input_data}")
        question = input_data["question"]
        cognitive_response = query.execute_service(question, adapter_cs)

        text_to_gpt = cognitive_response["text"]
        indexed_document = cognitive_response["document"]

        gpt_response = adapter_gpt.ask_openai(
            question, text_to_gpt, "question"
        )
        # indexed_document to list
        indexed_document = clean_text(indexed_document)

        indexed_document = indexed_document.split(",")

        logging.info("====================")
        logging.info("buscamos el texto indexado: ")
        logging.info(cognitive_response)
        logging.info("====================")

        logging.info("RESPUESTA DE GPT-3")
        logging.info(f"de acuerdo a {indexed_document}")
        logging.info(gpt_response)
        return OutputDataDto(gpt_response, indexed_document)
