




from src._shared.usecase.usecase_interface import UsecaseInterface
from src.account.domain.repository.user_repository_interface import UserRepositoryInterface


class DeleteUserUsecase(UsecaseInterface):

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, id):
        self.repository.delete(id)
        
    