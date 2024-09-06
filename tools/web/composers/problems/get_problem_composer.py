from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase
from web.controllers.problems.get_problem_controller import GetProblemController
from web.repository.problems.problem_repository import ProblemRepository


def get_problem_composer():
    repository = ProblemRepository()
    usecase = GetListProblemUsecase(repository=repository)
    controller = GetProblemController(usecase=usecase)

    return controller