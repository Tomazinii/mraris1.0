

import datetime
from typing import Any, List
from pydantic import BaseModel


class InputGetStudentFacadeDto(BaseModel):
    id: str

class OutputGetStudentFacadeDto(BaseModel):
    enrollment: str
    classroom_id: str
    name: str
    email: str

              



class OutputGetClassroomByIdFacadeDto(BaseModel):
    id: str
    teacher_email: str
    class_name: str
    


class OutputGetActivityByIdFacadeDto(BaseModel):
    id: str
    problem: List
    problem_name: str
    classroom_id: str
    category: str
    time: datetime.datetime

