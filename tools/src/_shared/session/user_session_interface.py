from abc import ABC, abstractmethod


class UserSessionInterface(ABC):

    @abstractmethod
    def create(self, jwt, jwt_secret, response, user_id):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, session_key):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, session_key):
        raise NotImplementedError
    
    @abstractmethod
    def verify(self, session_key):
        raise NotImplementedError
    