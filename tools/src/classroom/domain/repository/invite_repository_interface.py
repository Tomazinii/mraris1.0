

from abc import ABC, abstractmethod

from src.account.domain.entity.invite import InviteStudent


class InviteStudentRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input: InviteStudent):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, id: str):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_classroom(self, classroom_id: str):
        raise NotImplementedError
    
    def stamp(self, id):
        raise NotImplementedError
    
    
    