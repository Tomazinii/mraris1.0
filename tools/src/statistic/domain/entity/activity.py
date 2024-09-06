

import datetime
from typing import List


class ActivityData:
    __id: str
    __problem_id: int
    __problem: str
    __solution: List
    __classroom_id: str
    __time: datetime.datetime
    __category: str

    def __init__(self, id, problem_id, solution, problem, classroom_id, time, category):
        self.__problem = problem
        self.__problem_id = problem_id
        self.__solution = solution
        self.__id = id
        self.__classroom_id = classroom_id
        self.__time = time
        self.__category = category

    def get_category(self):
        return self.__category
    
    def get_time(self):
        return self.__time
    
    def get_classroom_id(self):
        return self.__classroom_id

    def get_id(self):
        return self.__id
    
    def get_problem_id(self):
        return self.__problem_id
    
    def get_solution(self):
        return self.__solution
    
    def get_problem(self):
        return self.__problem
    
