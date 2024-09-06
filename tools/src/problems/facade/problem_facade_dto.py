

import datetime
from typing import Any
from pydantic import BaseModel


class InputProblemFacadeDto(BaseModel):
    id: str

class OutputProblemFacadeDto(BaseModel):
    id: str
    list_name: str
    slug: str
    list_problem: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    comentary: str
