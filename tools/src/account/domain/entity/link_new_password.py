from src._shared.entity.invite_base import InviteBase
from src._shared.value_object.email import Email


class LinkNewPassword(InviteBase):
    __to: Email

    def __init__(self, id, time_expires):
        super().__init__(id, time_expires)

    def set_to(self, email: Email):
        self.__to = email

    def get_to(self):
        return self.__to.get_email()
    
    def get_time_expires(self):
        return super().get_time_expires()
    
    def get_id(self):
        return super().get_id()
    

    





    