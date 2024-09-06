

from abc import ABC, abstractmethod


class JwtServiceInterface(ABC):

    @abstractmethod
    def encode(self, data: any):
        raise NotImplementedError
    
    @abstractmethod
    def decode(self,data: any, secret_key: str):
        raise NotImplementedError