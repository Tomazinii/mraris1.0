

from src.account.usecase.link_set_new_password_usecase import LinkSetNewPasswordUsecase
from web.controllers.account.link_reset_password import LinkResetPasswordController
from web.repository.account.link_password_repository import LinkPasswordRepository
from web.sdk.email.email_service import EmailService


def link_reset_password_composer():

    email_service = EmailService()
    repository = LinkPasswordRepository()
    usecase = LinkSetNewPasswordUsecase(email_service=email_service, repository=repository)
    controller = LinkResetPasswordController(usecase=usecase)
    
    return controller