


from src.classroom.usecases.delete_activity_usecase import DeleteActivityUsecase
from web.controllers.classroom.delete_activity_controller import DeleteActivityController
from web.repository.classroom.activity_repository import ActivityRepository


def delete_activity_composer():
    repository = ActivityRepository()
    usecase = DeleteActivityUsecase(repository=repository)
    controller = DeleteActivityController(usecase=usecase)

    return controller