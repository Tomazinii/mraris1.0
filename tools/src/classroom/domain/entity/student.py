

from src._shared.entity.base_entity import Base
from src._shared.value_object.email import Email


class Student(Base):
    __name: str
    __email: Email
    __enrollment: str
    __classroom_id: str

    def __init__(self, id, created_at, updated_at, name, enrollment: str):
        super().__init__(id, created_at, updated_at)
        self.__name = name
        self.__enrollment = enrollment

    def set_email(self, email: Email):
        self.__email = email

    def get_email(self):
        return self.__email.get_email()
    
    def get_name(self):
        return self.__name
    
    def get_enrollment(self):
        return self.__enrollment
    
    def set_classroom_id(self, classroom_id):
        self.__classroom_id = classroom_id

    def get_classroom_id(self):
        return self.__classroom_id

    def change_id(self, id):
        self.__id = id