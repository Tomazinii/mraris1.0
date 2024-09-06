

from src.account.usecase.set_new_password_usecase import NewPasswordUsecase
from web.controllers.account.reset_password_controller import ResetPasswordController
from web.repository.account.link_password_repository import LinkPasswordRepository
from web.repository.account.user_repository import UserRepository


def reset_password_composer():

    link_repostory = LinkPasswordRepository()
    user_repository = UserRepository()
    usecase = NewPasswordUsecase(repository=user_repository, repository_link_password=link_repostory)
    controller = ResetPasswordController(usecase=usecase)

    return controller