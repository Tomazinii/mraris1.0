

from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.repository.student_repository_interface import StudentRepositoryInterface
from src.classroom.usecases.get_student_classroom_usecase_dto import OutputGetStudentDto



class GetStudentUsecase(UsecaseInterface):

    def __init__(self, repository: StudentRepositoryInterface):
        self.repository = repository

    def execute(self, student_id) -> OutputGetStudentDto:

        data = self.repository.get_by_id(id=student_id)

        output = OutputGetStudentDto(
            classroom_id=data.get_classroom_id(),
            enrollment=data.get_enrollment(),
            name=data.get_name(),
            email=data.get_email(),

        )

        return output
