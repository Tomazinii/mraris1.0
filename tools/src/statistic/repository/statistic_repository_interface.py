

from abc import ABC, abstractmethod

from src.statistic.domain.entity.result_activity import ResultActivity


class ResultActivityRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input: ResultActivity):
        raise NotImplementedError
    
    @abstractmethod
    def verify(self, user_id, activity_id, problem_id):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_classroom(self, classroom_id):
        raise NotImplementedError

    @abstractmethod
    def get_solved_activity(self, activity_id, user_id):
        raise NotImplementedError