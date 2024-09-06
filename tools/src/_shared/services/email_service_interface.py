

from abc import ABC, abstractmethod


class EmailServiceInterface(ABC):

    @abstractmethod
    def send(self, to, subject, content):
        raise NotImplementedError
        