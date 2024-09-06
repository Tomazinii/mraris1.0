


from typing import Any, List
from pydantic import BaseModel


class OutputBackMrplatoUsecaseDto(BaseModel):
    premisses: List
    conclusion: str
    new_lines: List


class InputBackMrplatoUsecaseDto(BaseModel):
    session_key: Any

