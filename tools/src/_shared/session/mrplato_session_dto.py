
import datetime
from typing import Any
from uuid import UUID
from pydantic import BaseModel


class MrplatoSessionDto(BaseModel):
    id: UUID 
    prover: Any
    time_session: Any
    num_backs: int = 0
    num_attempts: int = 0
    num_errors: int = 0
    timer: Any

