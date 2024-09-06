

from uuid import UUID
from pydantic import BaseModel


class InputChangePasswordDto(BaseModel):
    new_password: str
    session_key: UUID