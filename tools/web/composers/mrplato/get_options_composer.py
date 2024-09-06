from src.mrplato.usecase.get_options_usecase import GetOptionsUsecase
from src.problems.facade.problem_facade import ProblemFacade
from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase
from web.controllers.mrplato.get_options_controller import GetOptionController
from web.repository.problems.problem_repository import ProblemRepository
from web.sdk.mrplato.mrplato_service import ServiceMrplato
from web.session.mrplato_session import MrplatoSession

from web.sdk.mrplato.get_options import get_option as get_options_method

def get_options_composer():

    session = MrplatoSession()
    get_options = get_options_method
    service_mrplato = ServiceMrplato(get_option_method=get_options, prover=None, get_current_status_prover_method=None)
    usecase = GetOptionsUsecase(service=service_mrplato, session=session)
    controller = GetOptionController(usecase=usecase)

    return controller