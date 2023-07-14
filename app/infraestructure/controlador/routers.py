import logging
from fastapi import APIRouter, Request


from app.application.handler_query import HandlerQuery
from app.domain.modelo.output_data_dto import OutputDataDto
from app.domain.modelo.input_data_dto import InputDataDto


handler_query = HandlerQuery()

router = APIRouter()
api = "generate"


@router.post(f"/{api}/chat", response_model=object)
async def query_cognitive(request: Request) -> OutputDataDto:
    logging.warning(__name__)
    data = await request.json()
    return handler_query.execute(data)
