import abc
from domain.modelo.input_data_dto import InputDataDto


class OpenAIPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ask_openai(self, question: str, text: str, task: str):
        raise NotImplementedError
