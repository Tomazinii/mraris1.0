

from src.statistic.domain.entity.activity import ActivityData
from src.statistic.domain.entity.metrics import Metrics
from src.statistic.domain.entity.student import Student

class ResultActivity:
    __id: str
    __classroom_id: str
    __student: Student
    __mrplato_metrics: Metrics
    __activity: ActivityData

    def __init__(self, id: str):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_classroom_id(self, id: str):
        self.__classroom_id = id

    def get_classroom_id(self):
        return self.__classroom_id


    def set_student(self, student: Student):
        self.__student = student

    def get_student(self):
        return self.__student
    
    def set_mrplato_metrics(self, mrplato_metrics: Metrics):
        self.__mrplato_metrics = mrplato_metrics
    
    def get_mrplato_metrics(self):
        return self.__mrplato_metrics
    
    def set_activity(self, activity: ActivityData):
        self.__activity = activity

    def get_activity(self):
        return self.__activity
