

import datetime
from pydantic import BaseModel


class InputRegisterActivityUsecaseDto(BaseModel):
    id: str
    created_at: datetime.datetime
    time: datetime.datetime
    problem_id: str
    classroom_id: str
    category: str
    availability: bool