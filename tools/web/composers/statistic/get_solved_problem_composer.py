

from src.statistic.usecase.get_solved_activity_usecase import GetSolvedActivityUsecase
from web.controllers.statistic.get_solved_activity import GetSolvedActivityController
from web.repository.statistic.result_activity_repository import ResultActivityRepository


def get_solved_activity_composer():
    repository = ResultActivityRepository()
    usecase = GetSolvedActivityUsecase(repository=repository)
    controller = GetSolvedActivityController(usecase=usecase)
    return controller