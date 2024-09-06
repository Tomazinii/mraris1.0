

from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface


class DeleteActivityUsecase(UsecaseInterface):

    def __init__(self, repository: ActivityRepositoryInterface):
        self.repository = repository


    def execute(self, activity_id):
        self.repository.delete(activity_id)