

from src.account.facade.account_facade_interface import AccountFacadeInterface
from src.account.usecase.user_register_usecase import UserRegisterUsecase
from src.account.usecase.user_register_usecase_dto import InputUserRegisterUsecaseDto


class AccountFacade(AccountFacadeInterface):

    def __init__(self, register_usecase: UserRegisterUsecase):
        self.register_usecase = register_usecase

    def register_user(self, input: InputUserRegisterUsecaseDto) -> None:
        result = self.register_usecase.execute(input)
        return result