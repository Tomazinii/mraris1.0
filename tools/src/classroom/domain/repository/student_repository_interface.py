from abc import ABC, abstractmethod

from src.classroom.domain.entity.student import Student


class StudentRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input: Student):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id) -> Student:
        raise NotImplementedError
    
    @abstractmethod
    def get(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_all_by_classroom(self, classroom_id):
        raise NotImplementedError

    def verify_create(self, input: Student):
        raise NotImplementedError
    
