

from src.classroom.usecases.get_classroom_usecase import GetClassroomUsecase
from web.controllers.classroom.get_classroom_controller import GetClassroomController
from web.repository.classroom.classroom_repository import ClassroomRepository


def get_classroom_composer():
    repository = ClassroomRepository()
    usecase = GetClassroomUsecase(repository=repository)
    controller = GetClassroomController(usecase=usecase)
    return controller