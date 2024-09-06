

from src.mrplato.usecase.back_mrplato_usecase import BackMrplatoUsecase
from web.controllers.mrplato.back_mrplato_controller import BackStateMrplatoController
from web.sdk.mrplato.mrplato_service import ServiceMrplato
from web.session.mrplato_session import MrplatoSession
from web.sdk.mrplato.back_state_mrplato import back_state_mrplato

def back_mrplato_composer():
    session = MrplatoSession()
    back_mrplato = back_state_mrplato
    service = ServiceMrplato(back_state_mrplato=back_mrplato)
    usecase = BackMrplatoUsecase(session=session, service_back_mrplato=service)
    controller = BackStateMrplatoController(usecase=usecase)
    return controller