

from src.classroom.facade.classroom_facade import ClassroomFacade
from src.classroom.usecases.get_activity_by_id_usecase import GetActivityByIdUsecase
from src.classroom.usecases.get_student_classroom_usecase import GetStudentUsecase
from src.mrplato.usecase.prover_usecase import ProverUsecase
from src.problems.facade.problem_facade import ProblemFacade
from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase
from src.statistic.facade.statistic_facade import StatisticFacade
from src.statistic.usecase.register_result_activity_usecase import RegisterResultActivityUsecase
from web.controllers.mrplato.prover_mrplato_controller import MrplatoController
from web.repository.classroom.activity_repository import ActivityRepository
from web.repository.classroom.student_repository import StudentRepository
from web.repository.problems.problem_repository import ProblemRepository
from web.repository.statistic.result_activity_repository import ResultActivityRepository
from web.sdk.mrplato.get_user_solution import get_solution_service
from web.sdk.mrplato.mrplato_service import ServiceMrplato
from web.session.mrplato_session import MrplatoSession
from web.sdk.mrplato.prover import prover as prover_method


def mrplato_composer():
    session = MrplatoSession()
    prover = prover_method
    repository_result = ResultActivityRepository()
    repository_activity = ActivityRepository()
    get_activity_by_id_usecase = GetActivityByIdUsecase(repository=repository_activity)
    repository_student = StudentRepository()
    classroom_facade = ClassroomFacade(get_activity_by_id=get_activity_by_id_usecase, get_student=GetStudentUsecase(repository=repository_student))
    register_result_activity_usecase = RegisterResultActivityUsecase(repository=repository_result, activity_facade=classroom_facade, student_facade=classroom_facade)
    statistic = StatisticFacade(register_result_activity_usecase=register_result_activity_usecase)
    service_prover = ServiceMrplato(prover=prover, get_option_method=None, get_current_status_prover_method=None, get_solution_service_method=get_solution_service)
    usecase = ProverUsecase(service=service_prover, session=session, statistic_facade=statistic)
    controller = MrplatoController(usecase=usecase)
    return controller