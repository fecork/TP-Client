from unittest.mock import Mock
from domain.service.ask_generate import AskGenerate


def test_ask_generate_execute_service():
    question = "What is the meaning of life?"
    text = (
        "The meaning of life is a philosophical question concerning the"
        " significance of life or existence in general."
    )
    task = "text-generation"
    expected_response = (
        "The meaning of life is a philosophical question concerning the"
        " significance of life or existence in general."
    )
    port_mock = Mock()
    port_mock.ask_openai.return_value = expected_response

    ask_generate = AskGenerate()

    response = ask_generate.execute_service(question, text, task, port_mock)

    assert response == expected_response
