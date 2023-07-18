from pydantic import BaseModel


class InputDataDto(BaseModel):
    """
    Class InputDataDto
    Args: BaseModel
    Returns: str
    """

    question: str
