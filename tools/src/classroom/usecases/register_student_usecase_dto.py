

import datetime
from pydantic import BaseModel


class InputRegisterStudentUsecaseDto(BaseModel):
    created_at: datetime.datetime
    enrollment: str
    id: str
    username: str
    email: str
    updated_at: datetime.datetime
    password: str
    classroom_id: str
    invite_id: str