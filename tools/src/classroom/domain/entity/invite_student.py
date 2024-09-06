

import datetime
from src._shared.entity.base_entity import Base
from src._shared.errors.bad_request import BadRequestError
from src._shared.value_object.email import Email


class InvetStudent(Base):
    __title: str
    __content: str
    __to: Email
    __time_expires: datetime.datetime
    __classroom_id: str

    def __init__(self, id, created_at, updated_at, __classroom_id):
        super().__init__(id, created_at, updated_at)
        self.__classroom_id = __classroom_id

    
    def set_title(self, title: str):
        self.__title = title

    def get_title(self):
        return self.__title
    
    def set_content(self, content: str):
        self.__content = content

    def get_content(self):
        return self.__content
    
    def set_to(self, to: Email):
        self.__to = to

    def get_to(self):
        return self.__to.get_email()
    
    def set_time_expires(self, expires: datetime.datetime):
        self.__time_expires = expires



    def get_classroom_id(self):
        return self.__classroom_id