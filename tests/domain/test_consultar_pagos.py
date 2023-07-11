import logging
from unittest.mock import Mock
from app.domine.service.consultar_pagos import ConsultarPagos

from app.domine.modelo.arrendatario_dto import ArrendatarioDto


def test_calcular_deuda_pago_total():
    consultar = ConsultarPagos()
    port = Mock()
    respuesta = [
        {
            "documentoIdentificacionArrendatario": 111,
            "codigoInmueble": "111",
            "fechaPago": "2020-01-13",
            "valorPagado": 1000000,
        },
        {
            "documentoIdentificacionArrendatario": 111,
            "codigoInmueble": "222",
            "fechaPago": "2020-01-13",
            "valorPagado": 1000000,
        },
    ]
    port.consultar_totalidad_pagos.return_value = respuesta

    res = consultar.consultar_pagos(port)

    assert type(res) == list
