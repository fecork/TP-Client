import logging

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domine.port.port_mysql import portMysql


class ConsultarPagos:
    def consultar_pagos(self, port: "portMysql"):
        return port.consultar_totalidad_pagos()
