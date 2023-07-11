import abc

# from app.domine.modelo.arrendatario_dto import ArrendatarioDto


class CognitiveSearchPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query_cognitive_search(self, question):
        raise NotImplementedError
