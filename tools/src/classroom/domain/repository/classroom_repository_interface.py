from abc import ABC, abstractmethod
from src.account.domain.entity.invite import InviteStudent
from src.classroom.domain.entity.classroom import Classroom


class ClassroomRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input: Classroom):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, teacher_id):
        raise NotImplementedError