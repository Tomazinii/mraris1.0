
from abc import ABC, abstractmethod

from src.problems.domain.entity.problem import Problem


class ProblemRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input) -> any:
        raise Exception("method not implemented")
    
        
    @abstractmethod
    def get_all(self):
        raise Exception("method not implemented")
    
    def get_by_id(self, id) -> Problem:
        raise Exception("method not implemented")
    
    def update(self, input) -> Problem:
        raise Exception("method not implemented")
    
    def delete(self, id):
        raise Exception("method not implemented")

