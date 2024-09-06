
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.entity.activity import Activity
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface
from src.classroom.usecases.get_activity_by_id_usecase_dto import OutputGetActivityByIdDto


class GetActivityByIdUsecase(UsecaseInterface):

    def __init__(self, repository: ActivityRepositoryInterface):
        self.repository = repository

    def execute(self, activity_id: str) -> OutputGetActivityByIdDto:

        result: Activity = self.repository.get_by_id(id=activity_id)

        output = OutputGetActivityByIdDto(
            category=result.get_category(),
            classroom_id=result.get_classroom(),
            id=result.get_id(),
            problem=result.get_problem().get_list_problem(),
            problem_name=result.get_problem().get_name(),
            time=result.get_time(),
        )

        return output