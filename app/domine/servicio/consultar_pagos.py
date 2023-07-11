import logging

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domine.puerto.puerto_mysql import PuertoMysql


class ConsultarPagos:
    def consultar_pagos(self, puerto: "PuertoMysql"):
        return puerto.consultar_totalidad_pagos()
