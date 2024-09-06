

from src._shared.value_object.email import Email


class Student:
    __id: str
    __name: str
    __enrollment: str
    __email: Email

    def __init__(self, id: str, name:str, enrollment: str, email: Email):
        self.__id = id
        self.__name = name
        self.__enrollment = enrollment
        self.__email = email

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_enrollment(self):
        return self.__enrollment

    def get_email(self):
        return self.__email.get_email()
        

    