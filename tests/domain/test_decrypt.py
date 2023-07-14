import pytest
from app.domain.service.decrypt_64 import desencriptar


def test_desencriptar():
    data = "SGVsbG8gV29ybGQ="
    expected_output = "Hello World"
    assert desencriptar(data) == expected_output
