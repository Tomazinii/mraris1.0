

from pydantic import BaseModel




class InputNewPasswordDto(BaseModel):
    user_email: str
