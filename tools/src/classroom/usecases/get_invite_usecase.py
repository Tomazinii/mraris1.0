


from typing import List
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.repository.invite_repository_interface import InviteStudentRepositoryInterface
from src.classroom.usecases.get_invite_usecase_dto import OutputGetInviteUsecaseDto
from src.account.domain.entity.invite import InviteStudent

class GetInviteUsecase(UsecaseInterface):
    
    def __init__(self, repository: InviteStudentRepositoryInterface):
        self.repository = repository

    def execute(self, classroom_id: str) -> OutputGetInviteUsecaseDto:

        result: List[InviteStudent] = self.repository.get_by_classroom(classroom_id=classroom_id)

        output = [OutputGetInviteUsecaseDto(
            active=element.get_active(),
            to=element.get_to(),
            id=element.get_id()
        ) for element in result]

        return output