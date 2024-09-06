

from src._shared.entity.base_entity import Base
from src._shared.value_object.email import Email


class Teacher(Base):
    __name = str
    __email = Email

    def __init__(self, id, created_at, updated_at, name):
        super().__init__(id, created_at, updated_at)
        self.__name = name


    def set_email(self, email: Email):
        self.__email = email

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email.get_email()
