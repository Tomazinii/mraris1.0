

from pydantic import BaseModel


class OutputGetClassroomByIdDto(BaseModel):
    id: str
    teacher_email: str
    class_name: str
    