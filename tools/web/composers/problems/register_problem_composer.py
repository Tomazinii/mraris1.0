
from src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase
from web.controllers.problems.register_problem_controller import RegisterProblemController
from web.repository.problems.problem_repository import ProblemRepository


def register_problem_composer():
    repository = ProblemRepository()
    usecase = RegisterProblemUsecase(repository_service=repository)
    controller = RegisterProblemController(usecase=usecase)
    
    return controller