


import datetime
from uuid import UUID
from pydantic import BaseModel


class UserSessionDto(BaseModel):
    id: UUID
    token: str
    token_key: str
    time_session: datetime.datetime
    user_id: str


 