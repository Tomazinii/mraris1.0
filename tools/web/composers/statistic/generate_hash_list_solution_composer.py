

from src.statistic.usecase.generate_hash_solution_list_by_user_usecase import GenerateHashListSolution
from web.controllers.statistic.generate_hash_list_solution_controller import GenerateHashListSolutionController
from web.repository.account.user_repository import UserRepository
from web.repository.statistic.result_activity_repository import ResultActivityRepository
from web.sdk.jwt.jwt_service import JwtService


def generate_hash_list_composer():
    hash_service = JwtService()
    user_repository = UserRepository()
    repository = ResultActivityRepository()
    usecase = GenerateHashListSolution(repository=repository, hash_service=hash_service, user_repository=user_repository)
    controller = GenerateHashListSolutionController(usecase=usecase)

    return controller