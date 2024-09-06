

from src.classroom.usecases.register_activity_usecase import RegisterActivityUsecase
from src.problems.facade.problem_facade import ProblemFacade
from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase
from web.controllers.classroom.register_activity_controller import RegisterActivityController
from web.repository.classroom.activity_repository import ActivityRepository
from web.repository.problems.problem_repository import ProblemRepository


def register_activity_composer():
    repository = ActivityRepository()
    problem_repository = ProblemRepository()
    get_by_id_usecase=GetListProblemUsecase( repository=problem_repository)
    problem_facade = ProblemFacade(get_by_id_usecase=get_by_id_usecase)
    usecase = RegisterActivityUsecase(repository=repository, problem_facade=problem_facade)

    controller = RegisterActivityController(
        usecase=usecase
    )
    
    return controller