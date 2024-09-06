

from src.account.usecase.logout_usecase import LogoutUsecase
from web.controllers.account.logout_controller import LogoutController
from web.session.user_session import UserSession


def logout_composer():
    session = UserSession()
    usecase = LogoutUsecase(session=session)
    controller = LogoutController(usecase=usecase)
    return controller