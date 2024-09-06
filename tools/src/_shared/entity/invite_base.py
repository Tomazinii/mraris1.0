import datetime

from src._shared.errors.bad_request import BadRequestError


class InviteBase:
    __id: str
    __time_expires: datetime.datetime
    __active: bool = True


    def __init__(self, id, time_expires):
        self.__id = id
        self.__time_expires = time_expires


    def get_id(self):
        return self.__id
    
    def get_time_expires(self):
        return self.__time_expires

    def verify_time_expires(self):
        if self.__active == False:
            raise BadRequestError("invitation time has expired")

        if datetime.datetime.now() > self.__time_expires:
            self.__active = False
            raise BadRequestError("invitation time has expired")
        
    def set_active(self, active: bool):
        self.__active = active
    
    def get_active(self):
        return self.__active