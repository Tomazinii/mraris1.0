

from src.classroom.usecases.invite_usecase import InviteStudentUsecase
from web.controllers.classroom.invite_controller import InviteStudentController
from web.repository.classroom.invite_repository import InviteStudentRepository
from web.sdk.email.email_service import EmailService


def invite_composer():
    repository = InviteStudentRepository()
    email_service = EmailService()
    usecase = InviteStudentUsecase(email_service=email_service, repository=repository)
    controller = InviteStudentController(usecase=usecase)
    return controller