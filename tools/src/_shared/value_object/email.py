import re

from src._shared.errors.bad_request import BadRequestError

class Email:
    __email: str

    def __init__(self,email: str):
        self.validate(email=email)
        self.__email = email

    def validate(self, email: str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not (re.fullmatch(regex, email)):
            raise BadRequestError(f"Invalid email {email}")
        
    def get_email(self):
        return self.__email
        

