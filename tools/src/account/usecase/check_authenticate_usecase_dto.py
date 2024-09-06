


from typing import Any
from pydantic import BaseModel


class OutputCheckAuthenticateUsecaseDto(BaseModel):
    is_authenticated: bool
    data: Any