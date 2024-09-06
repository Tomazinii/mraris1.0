

from typing import List
from pydantic import BaseModel

from src._shared.value_object.email import Email


class InputInviteStudentDto(BaseModel):
    students_email: List
    classroom_id: str

