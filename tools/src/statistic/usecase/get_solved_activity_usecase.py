


from src._shared.usecase.usecase_interface import UsecaseInterface
from src.statistic.repository.statistic_repository_interface import ResultActivityRepositoryInterface
from src.statistic.usecase.get_solved_activity_dto import InputGetSolvedActivityDto, OutputGetSolvedActivityDto


class GetSolvedActivityUsecase(UsecaseInterface):

    def __init__(self, repository: ResultActivityRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputGetSolvedActivityDto) -> OutputGetSolvedActivityDto:

        data = self.repository.get_solved_activity(activity_id=input.activity_id, user_id=input.user_id)
        list_of_resolved_ativity = [result.problem_id for result in data]

        output = OutputGetSolvedActivityDto(
            activity_id=input.activity_id,
            list_of_resolved_ativity=list_of_resolved_ativity
        )

        return output

