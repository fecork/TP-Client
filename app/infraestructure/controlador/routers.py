from fastapi import APIRouter, logger, Request

from app.application.handler_query import HandlerQuery
from app.application.manejador_consulta import ManejadorConsultaPagos
from app.application.manejador_pagos import ManejadorPagos


handler_query = HandlerQuery()
manejador_pagos = ManejadorPagos()
manejador_consulta_pagos = ManejadorConsultaPagos()


router = APIRouter()
api = "generate"


@router.post(f"/{api}/chat", response_model=object)
async def query_cognitive(request: Request):
    logger.logger.warning(__name__)
    data = await request.json()
    return handler_query.execute(data)
