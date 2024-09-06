


from abc import ABC, abstractmethod

from src.account.facade.account_facade_dto import InputRegisterUserFacade


class AccountFacadeInterface(ABC):

    @abstractmethod
    def register_user(self, input: InputRegisterUserFacade):
        raise NotImplementedError