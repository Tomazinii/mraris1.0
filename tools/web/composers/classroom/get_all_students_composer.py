

from src.classroom.usecases.get_all_students_classroom_usecase import GetAllStudentsClassroomUsecase
from web.controllers.classroom.get_all_students_controller import GetAllStudentsController
from web.repository.classroom.student_repository import StudentRepository


def get_all_students_composer():
    repository = StudentRepository()
    usecase = GetAllStudentsClassroomUsecase(repository=repository)
    controller = GetAllStudentsController(usecase=usecase)
    return controller