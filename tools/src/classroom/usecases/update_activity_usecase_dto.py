


import datetime
from pydantic import BaseModel


class InputUpdateActivityUsecaseDto(BaseModel):
    activity_id: str
    time: datetime.datetime
    category: str
    availability:bool
