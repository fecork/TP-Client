from unittest.mock import Mock
from app.application.handler_query import HandlerQuery
from app.domain.modelo.output_data_dto import OutputDataDto


class TestHandlerQuery:
    def test_execute_handler_query(self):
        input_data = {"question": "control FAN"}

        expected_output = Mock()
        expected_output.text = (
            "Una API REST es un conjunto de restricciones arquitectónicas que"
            " se utilizan para construir aplicaciones web. Se basa en el"
            " protocolo HTTP y se utiliza para conectar aplicaciones y"
            " servicios en la web. Las API REST son populares porque son"
            " escalables, flexibles y fáciles de usar."
        )
        expected_output.indexed_document = [
            "API REST",
            "HTTP",
            "aplicaciones web",
        ]
        query_cs_mock = Mock()
        query_cs_mock.execute_service.return_value = {
            "text": (
                "Una API REST es un conjunto de restricciones arquitectónicas"
                " que se utilizan para construir aplicaciones web. Se basa en"
                " el protocolo HTTP y se utiliza para conectar aplicaciones y"
                " servicios en la web. Las API REST son populares porque son"
                " escalables, flexibles y fáciles de usar."
            ),
            "document": "API REST, HTTP, aplicaciones web",
        }
        query_gpt_mock = Mock()
        query_gpt_mock.execute_service.return_value = (
            "Una API REST es un conjunto de restricciones arquitectónicas que"
            " se utilizan para construir aplicaciones web. Se basa en el"
            " protocolo HTTP y se utiliza para conectar aplicaciones y"
            " servicios en la web. Las API REST son populares porque son"
            " escalables, flexibles y fáciles de usar."
        )
        adapter_gpt_mock = Mock()
        adapter_gpt_mock.ask_openai.return_value = expected_output.text
        adapter_cs_mock = Mock()
        adapter_cs_mock.search.return_value = {
            "text": expected_output.text,
            "document": expected_output.indexed_document,
        }
        handler = HandlerQuery()
        handler.query_cs = query_cs_mock
        handler.query_gpt = query_gpt_mock
        handler.adapter_gpt = adapter_gpt_mock
        handler.adapter_cs = adapter_cs_mock
        output = handler.execute(input_data)
        assert isinstance(output, OutputDataDto)
