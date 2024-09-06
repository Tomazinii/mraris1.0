

from src.classroom.usecases.update_activity_usecase import UpdateActivityUsecase
from web.controllers.classroom.update_activity_controller import UpdateActivityController
from web.repository.classroom.activity_repository import ActivityRepository


def update_activity_composer():
    repository = ActivityRepository()
    usecase = UpdateActivityUsecase(repository=repository)
    controller = UpdateActivityController(usecase=usecase)

    return controller