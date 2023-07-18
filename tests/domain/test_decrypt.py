import pytest
from domain.service.decrypt_64 import descrypt


def test_descrypt():
    data = "SGVsbG8gV29ybGQ="
    expected_output = "Hello World"
    assert descrypt(data) == expected_output
