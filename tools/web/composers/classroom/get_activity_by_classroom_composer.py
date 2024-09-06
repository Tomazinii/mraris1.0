


from src.classroom.usecases.get_activity_by_classroom_usecase import GetActivityByClassroomUsecase
from web.controllers.classroom.get_activity_by_classroom_controller import GetActivityController
from web.repository.classroom.activity_repository import ActivityRepository


def get_activity_by_classroom_composer():

    repository = ActivityRepository()
    usecase = GetActivityByClassroomUsecase(repository=repository)
    controller = GetActivityController(usecase=usecase)
    return controller