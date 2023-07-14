from unittest.mock import MagicMock
from app.domain.service.search_cognitive import SearchCognitive


class TestSearchCognitive:
    def test_execute_service(self):
        port = MagicMock()
        port.query_cognitive_search.return_value = "This is a cognitive search"
        service = SearchCognitive()
        result = service.execute_service("What is cognitive search?", port)
        port.query_cognitive_search.assert_called_once_with(
            "What is cognitive search?"
        )
        assert result == "This is a cognitive search"
