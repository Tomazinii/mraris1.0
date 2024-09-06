
from abc import ABC, abstractmethod


class UsecaseInterface(ABC):

    @abstractmethod
    def execute(self) -> any:
        raise Exception("method not implemented")