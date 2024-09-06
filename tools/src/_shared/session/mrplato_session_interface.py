

from abc import ABC, abstractmethod


class MrplatoSessionInterface(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, session_key):
        raise NotImplementedError
    
    @abstractmethod
    def restart(self, session_key):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, session_key):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, session_key, data_session):
        raise NotImplementedError
    
    @abstractmethod
    def verify(self, session_key, response):
        raise NotImplementedError
