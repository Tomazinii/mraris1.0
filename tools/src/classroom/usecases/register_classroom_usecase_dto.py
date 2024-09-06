

import datetime
from pydantic import BaseModel


class InputRegisterClassroomDto(BaseModel):
    id: str
    class_name: str
    teacher_email: str
    teacher_name: str
    teacher_id: str
    teacher_created: datetime.datetime
    teacher_updated: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime


class OutputRegisterClassroomDto(BaseModel):
    id: str
    class_name: str
    teacher_email: str
    teacher_name: str
    created_at: datetime.datetime