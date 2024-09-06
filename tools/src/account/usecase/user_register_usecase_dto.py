

from datetime import datetime
from pydantic import BaseModel


class InputUserRegisterUsecaseDto(BaseModel):
    created_at: datetime
    email: str
    id: str
    password: str
    updated_at: datetime
    username: str
    is_admin: bool