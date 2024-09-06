

from abc import ABC, abstractmethod



class LinkPasswordRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input):
        raise NotImplementedError
    
    
    @abstractmethod
    def stamp(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, id):
        raise NotImplementedError

    
    
    