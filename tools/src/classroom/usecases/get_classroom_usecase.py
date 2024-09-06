

from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.repository.classroom_repository_interface import ClassroomRepositoryInterface
from src.classroom.usecases.get_classroom_usecase_dto import OutputGetClassroomUsecaseDto

class GetClassroomUsecase(UsecaseInterface):

    def __init__(self, repository: ClassroomRepositoryInterface):
        self.repository = repository

    def execute(self, teacher_id) -> OutputGetClassroomUsecaseDto:
        classrooms = self.repository.get(teacher_id=teacher_id)
        output = OutputGetClassroomUsecaseDto(
            classrooms=classrooms
        )
        return output
