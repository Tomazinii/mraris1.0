from src._shared.entity.invite_base import InviteBase
from src._shared.value_object.email import Email


class InviteStudent(InviteBase):
    __classroom_id: str
    __to: Email

    def __init__(self, id, time_expires, classroom_id):
        super().__init__(id, time_expires)
        self.__classroom_id = classroom_id

    def set_to(self, email: Email):
        self.__to = email

    def get_to(self):
        return self.__to.get_email()
    
    def get_time_expires(self):
        return super().get_time_expires()
    
    def get_id(self):
        return super().get_id()
    
    def get_classroom_id(self):
        return self.__classroom_id
    





    