

import datetime
from typing import Any, List
from pydantic import BaseModel


class InputRegisterActivityByInsertUsecaseDto(BaseModel):
    category: str
    classroom_id: str
    created_at: datetime.datetime
    id: str
    updated_at: datetime.datetime
    time: datetime.datetime
    availability: bool

    problem_id: str
    problem_list_name: str
    problem_comentary: str
    problem_created_at: datetime.datetime
    problem_list_problem: Any
    problem_updated_at: datetime.datetime
    