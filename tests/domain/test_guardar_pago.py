import logging
from unittest.mock import Mock
from app.domine.service.guardar_pago import GuardarPago
from app.domine.modelo.arrendatario_dto import ArrendatarioDto


def test_guardar_pago():
    guardar = GuardarPago()
    port = Mock()

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    port.service.return_value = None

    res = guardar.service(arrendatario, port)

    assert res == None


def test_consultar():
    guardar = GuardarPago()
    port = Mock()

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    port.consultar_pago.return_value = None

    res = guardar.consultar(arrendatario, port)

    assert res == None


def test_actualizar():
    guardar = GuardarPago()
    port = Mock()

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    port.actualizar_pago.return_value = None

    res = guardar.actualizar(arrendatario, port)

    assert res == None
