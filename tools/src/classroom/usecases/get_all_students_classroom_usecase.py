


from typing import List
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.entity.student import Student
from src.classroom.domain.repository.student_repository_interface import StudentRepositoryInterface
from src.classroom.usecases.get_all_students_classroom_usecase_dto import OutputGetAllStudentUsecaseDto


class GetAllStudentsClassroomUsecase(UsecaseInterface):
    
    def __init__(self, repository: StudentRepositoryInterface):
        self.repository = repository

    def execute(self, classroom_id) -> OutputGetAllStudentUsecaseDto:
        result: List[Student]= self.repository.get_all_by_classroom(classroom_id=classroom_id)

        output = [OutputGetAllStudentUsecaseDto(
            email=element.get_email(),
            enrollment=element.get_enrollment(),
            name=element.get_name()
        ) for element in result]
        
        return output