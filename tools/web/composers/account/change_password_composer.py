

from src.account.usecase.change_password_usecase import ChangePasswordUsecase
from web.controllers.account.change_password_controller import ChangePasswordController
from web.repository.account.user_repository import UserRepository
from web.session.user_session import UserSession


def change_password_composer():
    repository = UserRepository()
    session = UserSession()
    usecase = ChangePasswordUsecase(repository=repository, session=session)
    controller = ChangePasswordController(usecase=usecase)
    return controller