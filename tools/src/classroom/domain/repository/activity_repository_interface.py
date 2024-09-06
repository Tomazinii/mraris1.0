

from abc import ABC, abstractmethod
from typing import List

from src.classroom.domain.entity.activity import Activity


class ActivityRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input: Activity):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_classroom(self, classroom_id):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def update_availabity(self, list_activity_id_time_expired: List):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, input):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id):
        raise NotImplementedError