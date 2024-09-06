
from src._shared.services.jwt_service_interface import JwtServiceInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.account.domain.entity.user import User
from src.account.domain.repository.user_repository_interface import UserRepositoryInterface
from src.statistic.repository.statistic_repository_interface import ResultActivityRepositoryInterface
from src.statistic.usecase.get_solved_activity_dto import InputGetSolvedActivityDto, OutputGetSolvedActivityDto


class GenerateHashListSolution(UsecaseInterface):

    def __init__(self, repository: ResultActivityRepositoryInterface, user_repository: UserRepositoryInterface, hash_service: JwtServiceInterface):
        self.repository = repository
        self.user_repository = user_repository
        self.hash_service = hash_service

    def execute(self, input: InputGetSolvedActivityDto):

        data = self.repository.get_solved_activity(activity_id=input.activity_id, user_id=input.user_id)
        list_of_resolved_ativity = [result.problem_id for result in data]
        data_user: User = self.user_repository.get_by_id(id=input.user_id)

        encoded, secret = self.hash_service.encode(
            data={
                "user_id": f"{data_user.get_id()}",
                "email": f"{data_user.get_email()}",
                "username": f"{data_user.get_username()}",
                "list_of_resolved_ativity": list_of_resolved_ativity,
                "activity_id": f"{input.activity_id}"
            },
            jwt_secret="6d60d7eb5f34a80981357cea2902117e"
        )

        return encoded

