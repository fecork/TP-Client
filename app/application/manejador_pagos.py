from app.domine.service.guardar_pago import GuardarPago
from app.domine.service.validar_fechas import ValidarFechas
from app.domine.excepciones.error_del_negocio import ErrorDelNegocio
from app.domine.service.calcular_deuda import CalcularDeuda

from app.infraestructure.adapter.mysql.adapter_mysql import adapterMysql

import logging


guardar = GuardarPago()
adapter = adapterMysql()
validar_fecha = ValidarFechas()
error_del_negocio = ErrorDelNegocio()
calcular_deuda = CalcularDeuda()


class ManejadorPagos:
    validar_fecha = ValidarFechas()

    def ejecutar(self, arrendatario):
        existe_arrendatario = guardar.consultar(arrendatario, adapter)
        arrendatario = validar_fecha.formato_fecha(arrendatario)
        if arrendatario is False:
            return error_del_negocio.respuesta_error(404, "formato")

        es_impar = validar_fecha.fecha_impar(arrendatario)
        if es_impar:
            return error_del_negocio.respuesta_error(400, "impar")

        if existe_arrendatario is False:
            guardar.service(arrendatario, adapter)
            return calcular_deuda.calcular_deuda(arrendatario, adapter)

        if existe_arrendatario is not False:
            guardar.actualizar(arrendatario, adapter)
            return calcular_deuda.calcular_deuda(arrendatario, adapter)
