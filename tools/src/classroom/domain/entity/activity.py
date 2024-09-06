
import datetime
from src._shared.entity.base_entity import Base
from src.classroom.domain.entity.problem import Problem

class Activity(Base):
    __problem: Problem
    __classroom_id: str
    __category: str
    __time: datetime.datetime
    __availability: bool = True

    def __init__(self, id, created_at, updated_at):
        super().__init__(id, created_at, updated_at)

    def set_problem(self, problem: Problem):
        self.__problem = problem

    def get_problem(self):
        return self.__problem
    
    def set_classroom(self, classroom_id: str):
        self.__classroom_id = classroom_id

    def get_classroom(self):
        return self.__classroom_id

    def set_category(self, category):
        self.__category = category
    
    def get_category(self):
        return self.__category

    def set_time(self, time):
        self.__time = time

    def verify_time_expired(self) -> bool:
        if datetime.datetime.now() > self.__time:
            self.__availability = False

    def set_availability(self, availability: bool):
        self.__availability = availability
    
    def get_availability(self):
        return self.__availability
    
    def get_time(self):
        return self.__time
    
    
        


    


