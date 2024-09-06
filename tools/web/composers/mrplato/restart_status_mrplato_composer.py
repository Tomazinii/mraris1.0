

from src.mrplato.usecase.restart_status_mrplato_usecase import RestartStatusMrplatoUsecase
from web.controllers.mrplato.restart_status_mrplato_controller import RestartStatusMrplatoController
from web.session.mrplato_session import MrplatoSession


def retart_status_mrplato_composer():
    session = MrplatoSession()
    usecase = RestartStatusMrplatoUsecase(session=session)
    controller = RestartStatusMrplatoController(usecase=usecase)

    return controller