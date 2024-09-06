

import datetime
from typing import List
from pydantic import BaseModel


class OutputGetActivityByIdDto(BaseModel):
    id: str
    problem: List
    problem_name: str
    classroom_id: str
    category: str
    time: datetime.datetime
