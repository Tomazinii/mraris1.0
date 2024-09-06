

from src.classroom.usecases.check_invite_usecase import CheckInviteUsecase
from web.controllers.classroom.check_invite_controller import CheckInviteController
from web.repository.classroom.invite_repository import InviteStudentRepository


def check_invite_composer():
    repository = InviteStudentRepository()
    usecase = CheckInviteUsecase(repository=repository)
    controller = CheckInviteController(usecase=usecase)
    return controller