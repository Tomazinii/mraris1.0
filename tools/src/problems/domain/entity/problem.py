import datetime
from src.problems.domain.value_object import ListProblem
from src._shared.entity import Base
from src.problems.domain.value_object.slug import Slug


class PropsProblemType:
    def __init__(self, id, created_at, updated_at, comentary, list_name):
        self.id: str = id
        self.created_at: datetime.datetime = created_at
        self.updated_at: datetime.datetime = updated_at
        self.comentary: str = comentary
        self.list_name: str = list_name

class Problem(Base):
    __list_name: str
    __comentary: str = ""
    __list_problem: ListProblem
    __slug: Slug

    def __init__(self, props: PropsProblemType):
        super().__init__(props.id, props.created_at, props.updated_at)
        self.__list_name = props.list_name
        self.__comentary = props.comentary
        

    def get_list_name(self):
        return self.__list_name
    
    def get_comentary(self):
        return self.__comentary
    
    def get_list_problem(self):
        return self.__list_problem

    def get_slug(self):
        return self.__slug

    def set_list_problem(self, list_problem: ListProblem):
        self.__list_problem = list_problem

    def set_slug(self, slug: Slug):
        self.__slug = slug
        