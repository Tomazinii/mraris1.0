

from typing import List
from pydantic import BaseModel


class OutputGetAllProblemUsecaseDto(BaseModel):
    problems: List