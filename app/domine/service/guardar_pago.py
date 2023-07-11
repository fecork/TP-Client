import logging

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domine.port.port_mysql import portMysql


class GuardarPago:
    def service(self, arrendatario, port: "portMysql"):
        port.insertar(self, arrendatario)

    def consultar(self, arrendatario, port: "portMysql"):
        return port.consultar_pago(self, arrendatario)

    def actualizar(self, arrendatario, port: "portMysql"):
        port.actualizar_pago(self, arrendatario)
