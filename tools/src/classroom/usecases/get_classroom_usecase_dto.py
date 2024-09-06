
import datetime
from typing import Any, List
from pydantic import BaseModel


class ClassroomDto(BaseModel):
    id: str
    class_name: str
    created_at: datetime.datetime
    teacher_name: str
    teacher_email: str


class OutputGetClassroomUsecaseDto(BaseModel):
    classrooms: Any