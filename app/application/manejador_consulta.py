from app.domine.service.consultar_pagos import ConsultarPagos
from app.domine.excepciones.error_del_negocio import ErrorDelNegocio

from app.infraestructure.adapter.mysql.adapter_mysql import adapterMysql

import logging


consultar = ConsultarPagos()
adapter = adapterMysql()
error_del_negocio = ErrorDelNegocio()


class ManejadorConsultaPagos:
    def ejecutar(self):
        return consultar.consultar_pagos(adapter)
