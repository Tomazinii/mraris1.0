

from pydantic import BaseModel


class InputLoginUsecase(BaseModel):
    email: str
    password: str