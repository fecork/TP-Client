from dataclasses import dataclass


@dataclass
class OutputDataDto:
    response: dict[any, any]
    document: list[str, any]
