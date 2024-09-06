

from pydantic import BaseModel


class InputSetNewPasswordDto(BaseModel):
    new_password: str
    user_email: str
    link_id: str