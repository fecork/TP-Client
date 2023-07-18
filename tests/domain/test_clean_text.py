import pytest
from domain.service.clean_text import clean_text


def test_clean_text():
    text = "This is a test. \n \n It has multiple lines. [With brackets]"
    expected_result = "This is a test. It has multiple lines. With brackets"
    print(text)
    print(expected_result)
    assert clean_text(text) == expected_result
