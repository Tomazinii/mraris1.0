

from typing import List
from pydantic import BaseModel


class InputGetSolvedActivityDto(BaseModel):
    activity_id: str 
    user_id: str

class OutputGetSolvedActivityDto(BaseModel):
    activity_id: str
    list_of_resolved_ativity: List