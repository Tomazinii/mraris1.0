

from pydantic import BaseModel


class OutputCheckInviteDto(BaseModel):
    is_valid: bool
    message: str