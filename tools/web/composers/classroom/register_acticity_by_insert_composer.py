
from src.classroom.usecases.register_activity_by_insert import RegisterActivityByInsertUsecase
from src.problems.facade.problem_facade import ProblemFacade
from src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase
from web.controllers.classroom.register_activity_by_insert_controller import RegisterActivityByInsertController
from web.repository.classroom.activity_repository import ActivityRepository
from web.repository.problems.problem_repository import ProblemRepository


def register_activity_by_insert_composer():
    repository_problem = ProblemRepository()
    register_problem_usecase = RegisterProblemUsecase(repository_service=repository_problem)
    problem_facade = ProblemFacade(get_by_id_usecase=None, register_problem_by_insert_usecase=register_problem_usecase)
    repository = ActivityRepository()
    usecase = RegisterActivityByInsertUsecase(problem_facade=problem_facade, repository=repository)
    controller = RegisterActivityByInsertController(usecase=usecase)
    return controller