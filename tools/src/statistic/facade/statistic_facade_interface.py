
from abc import ABC, abstractmethod

from src.statistic.facade.statistic_facade_dto import InputRegisterResultActivityFacade


class StatisticFacadeInterface(ABC):

    @abstractmethod
    def register_result_activity(self, input: InputRegisterResultActivityFacade):
        raise NotImplementedError