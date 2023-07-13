import logging
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domine.port.cognitve_search_port import CognitiveSearchPort


class SearchCognitive:
    """
    SearchCognitive class
    """

    logging.warning(__name__)

    def execute_service(self, question, port: "CognitiveSearchPort"):
        """
        execute_service cognitive search
        Args: question
        Returns: cognitive search
        """
        return port.query_cognitive_search(question)
