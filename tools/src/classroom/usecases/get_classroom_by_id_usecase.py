

from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.entity.classroom import Classroom
from src.classroom.domain.repository.classroom_repository_interface import ClassroomRepositoryInterface
from src.classroom.usecases.get_classroom_by_id_usecase_dto import OutputGetClassroomByIdDto


class GetClassroomByIdUsecase(UsecaseInterface):

    def __init__(self, repository: ClassroomRepositoryInterface):
        self.repository = repository

    def execute(self, classroom_id:str) -> OutputGetClassroomByIdDto:
        result = self.repository.get_by_id(id=classroom_id)

        output = OutputGetClassroomByIdDto(
            class_name = result.class_name,
            id=result.id,
            teacher_email = result.teacher_email
        )

        return output