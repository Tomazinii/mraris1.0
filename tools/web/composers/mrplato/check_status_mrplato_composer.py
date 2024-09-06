


from src.mrplato.usecase.check_status_mrplato_usecase import CheckStatusMrplatoUsecase
from web.controllers.mrplato.check_status_mrplato_controller import CheckStatusMrplatoController
from web.sdk.mrplato.mrplato_service import ServiceMrplato
from web.session.mrplato_session import MrplatoSession
from web.sdk.mrplato.get_current_status_prover import get_current_status_prover

def check_status_mrplato_composer():
    get_current_status = get_current_status_prover
    service = ServiceMrplato(prover=None, get_option_method=None, get_current_status_prover_method=get_current_status)
    session = MrplatoSession()
    usecase = CheckStatusMrplatoUsecase(session=session, service=service)
    controller = CheckStatusMrplatoController(usecase=usecase)
    return controller