


from abc import ABC, abstractmethod


class CsvServiceInterface(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError