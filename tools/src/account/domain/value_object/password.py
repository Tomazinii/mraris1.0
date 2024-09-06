
import hashlib
import os

from src._shared.errors.bad_request import BadRequestError

class Password:
    __password: str

    def __init__(self, password: str):
        self.validate(password=password)
        self.__password = self.encrypt(password)

    def validate(self, password):
        if len(password) < 8:
            raise BadRequestError("the password must be at least 8 characters")

    def encrypt(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def get_password(self):
        return self.__password
    
    def change_password(self, new_password):
        self.validate(password=new_password)
        self.__password = self.encrypt(new_password)
        
    