


from src.account.usecase.check_link_reset_password import CheckLinkResetPasswordUsecase
from web.controllers.account.check_link_reset_password_controller import CheckLinkResetPasswordController
from web.repository.account.link_password_repository import LinkPasswordRepository


def check_link_reset_password_composer():

    repository = LinkPasswordRepository()
    usecase = CheckLinkResetPasswordUsecase(repository=repository)
    controller = CheckLinkResetPasswordController(usecase=usecase)

    return controller