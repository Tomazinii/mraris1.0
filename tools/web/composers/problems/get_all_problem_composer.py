

from src.problems.usecase.get_all_problem_usecase import GetAllProblemsUsecase
from web.controllers.problems.get_all_problems_controller import GetAllProblemsController
from web.repository.problems.problem_repository import ProblemRepository


def get_all_problem_composer():
    repository = ProblemRepository()
    usecase = GetAllProblemsUsecase(repository=repository)
    controller = GetAllProblemsController(usecase=usecase)
    return controller