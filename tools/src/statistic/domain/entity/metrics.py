



import datetime


class Metrics:
    __id: str
    __time: datetime.datetime
    __num_attempt: int
    __num_backs: int
    __errors: int

    def __init__(self, id, time, num_attempt, num_backs, errors):
        self.__id = id
        self.__time = time
        self.__num_attempt = num_attempt
        self.__num_backs = num_backs
        self.__errors = errors

    def get_id(self):
        return self.__id
    
    def get_time(self):
        return self.__time
    
    def get_num_attempts(self):
        return self.__num_attempt
    
    def get_errors(self):
        return self.__errors
    
    def get_num_backs(self):
        return self.__num_backs