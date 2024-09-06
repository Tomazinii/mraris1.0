

import datetime
from typing import Any, List
from pydantic import BaseModel


class InputRegisterResultActivityFacade(BaseModel):
    id: str
    classroom_id: str
    student_id: str
    activity_id: str
    problem_id: int
    time: Any
    num_atempet: int
    num_backs: int
    num_errors: int
    solution: List



