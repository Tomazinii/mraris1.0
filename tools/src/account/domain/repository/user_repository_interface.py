

from abc import ABC, abstractmethod

from src.account.domain.entity.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_email(self, email):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def check_register(self, email: str):
        raise NotImplementedError

    @abstractmethod
    def change_password(self, user_id: str, password: str):
        raise NotImplementedError
