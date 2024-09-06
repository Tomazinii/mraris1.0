

from src.classroom.usecases.get_invite_usecase import GetInviteUsecase
from web.controllers.classroom.get_invite_by_classroom_controller import GetInviteByClassroomController
from web.repository.classroom.invite_repository import InviteStudentRepository


def get_invite_by_classroom_composer():
    repository = InviteStudentRepository()
    usecase = GetInviteUsecase(repository=repository)
    controller = GetInviteByClassroomController(usecase=usecase)
    return controller