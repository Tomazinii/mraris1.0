
from typing import List
from pydantic import BaseModel


class OutputGetAllStudentUsecaseDto(BaseModel):
    name: str
    email: str
    enrollment: str