from fastapi import APIRouter

from app.application.handler_query import HandlerQuery
from app.application.manejador_consulta import ManejadorConsultaPagos
from app.application.manejador_pagos import ManejadorPagos
from app.domine.modelo.arrendatario_dto import ArrendatarioDto


handler_query = HandlerQuery()
manejador_pagos = ManejadorPagos()
manejador_consulta_pagos = ManejadorConsultaPagos()


router = APIRouter()
api = "api"


@router.get(f"/{api}/query_cognitive", response_model=object)
async def query_cognitive() -> object:
    return handler_query.execute()


@router.get(f"/{api}/pagos", response_model=object)
async def test() -> object:
    return manejador_consulta_pagos.ejecutar()


@router.post(f"/{api}/pagos", response_model=object)
async def test(arrendatario: ArrendatarioDto) -> ArrendatarioDto:
    return manejador_pagos.ejecutar(arrendatario)
