



from src.classroom.usecases.get_classroom_by_id_usecase import GetClassroomByIdUsecase
from web.controllers.classroom.get_classroom_controller import GetClassroomController
from web.repository.classroom.classroom_repository import ClassroomRepository


def get_classroom_by_id_composer():
    repository = ClassroomRepository()
    usecase = GetClassroomByIdUsecase(repository=repository)
    controller = GetClassroomController(usecase=usecase)

    return controller