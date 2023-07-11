import logging

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domine.port.port_mysql import portMysql


class CalcularDeuda:
    def calcular_deuda(self, arrendatario, port: "portMysql"):
        arriendo_total = 1000000
        pago_actual = port.consultar_pago(self, arrendatario)

        abono_actual = arrendatario.valorPagado
        total_pagado = pago_actual + abono_actual
        deuda_total = arriendo_total - total_pagado

        if deuda_total > 0:
            respuesta = (
                "Gracias por tu abono sin embargo recuerda que te hace"
                f" falta pagar ${deuda_total}"
            )
        if deuda_total <= 0:
            respuesta = "gracias por pagar todo tu arriendo"
        return respuesta
