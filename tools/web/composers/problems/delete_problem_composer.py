

from src.problems.usecase.delete_list_problem_usecase import DeleteProblemUsecase
from web.controllers.problems.delete_problem_controller import DeleteProblemController
from web.repository.problems.problem_repository import ProblemRepository


def delete_problem_composer():
    repository = ProblemRepository()
    usecase = DeleteProblemUsecase(repository=repository)
    controller = DeleteProblemController(usecase=usecase)
    return controller