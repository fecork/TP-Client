from pydantic import BaseModel


class OutputDataDto(BaseModel):
    """
    Class OutputDataDto
    Args: BaseModel
    Returns: str, list[str]
    """

    response: str
    document: list[str]
