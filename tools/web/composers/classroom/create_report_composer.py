

from src.statistic.usecase.create_report_usecase import CreateReportUsecase
from web.controllers.classroom.create_report_controller import CreateReportController
from web.repository.statistic.result_activity_repository import ResultActivityRepository


def create_report_composer():
    repository = ResultActivityRepository()
    usecase =CreateReportUsecase(repository=repository)
    controller = CreateReportController(usecase=usecase)
    return controller