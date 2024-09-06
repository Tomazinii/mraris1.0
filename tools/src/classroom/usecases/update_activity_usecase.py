


from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface
from src.classroom.usecases.update_activity_usecase_dto import InputUpdateActivityUsecaseDto


class UpdateActivityUsecase(UsecaseInterface):
    
    def __init__(self, repository: ActivityRepositoryInterface):
        self.repository = repository

    
    def execute(self, input: InputUpdateActivityUsecaseDto):
        self.repository.update(input=input)
