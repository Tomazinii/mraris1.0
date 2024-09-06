

from src.classroom.usecases.register_classroom_usecase import RegisterClassroomUsecase
from web.controllers.classroom.classroom_controller import ClassroomController
from web.repository.classroom.classroom_repository import ClassroomRepository


def classroom_composer():
    repository = ClassroomRepository()
    usecase = RegisterClassroomUsecase(repository=repository)
    controller = ClassroomController(usecase=usecase)
    return controller