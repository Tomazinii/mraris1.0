


from typing import Any, List
from pydantic import BaseModel


class InputCheckStatusMrplatoUsecaseDto(BaseModel):
    session_key: Any
    problem: str


class OutputCheckStatusMrplatoUsecaseDto(BaseModel):
    premisses: List
    conclusion: str
    new_lines: List