import abc
from app.domine.modelo.input_data_dto import InputDataDto


class CognitiveSearchPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query_cognitive_search(self, input_data: InputDataDto):
        raise NotImplementedError
