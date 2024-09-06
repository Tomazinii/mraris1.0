

import datetime
from typing import List
from pydantic import BaseModel


class OutputGetActivityByClassroomDto(BaseModel):
    id: str
    category: str
    time: datetime.datetime
    problem: List
    problem_id: str
    problem_name: str
    problem_slug: str
    classroom_id: str
    availability: bool 
