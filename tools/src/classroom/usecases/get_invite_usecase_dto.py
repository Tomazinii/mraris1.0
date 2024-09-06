

from pydantic import BaseModel


class OutputGetInviteUsecaseDto(BaseModel):
    id: str
    to: str
    active: bool
