

import datetime
from typing import List
from pydantic import BaseModel

class InputRegisterResultActivityUsecaseDto(BaseModel):
    id: str
    classroom_id: str
    student_id: str
    activity_id: str
    problem_id: int
    time: datetime.datetime
    num_atempet: int
    num_backs: int
    num_errors: int
    solution: List
