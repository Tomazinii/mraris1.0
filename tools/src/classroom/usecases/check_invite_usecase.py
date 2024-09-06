

from src._shared.usecase.usecase_interface import UsecaseInterface

from src.classroom.domain.repository.invite_repository_interface import InviteStudentRepositoryInterface
from src.classroom.usecases.check_invite_usecase_dto import OutputCheckInviteDto


class CheckInviteUsecase(UsecaseInterface):

    def __init__(self, repository: InviteStudentRepositoryInterface):
        self.repository = repository

    def execute(self, invite_id: str):
        invite = self.repository.get(id=invite_id)
        invite.verify_time_expires()



        