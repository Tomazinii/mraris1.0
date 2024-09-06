

import datetime
from pydantic import BaseModel


class InputRegisterUserFacade(BaseModel):
    created_at: datetime.datetime
    email: str
    id: str
    password: str
    updated_at: datetime.datetime
    username: str
    is_admin: bool