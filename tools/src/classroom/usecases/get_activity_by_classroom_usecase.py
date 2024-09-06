


import datetime
from src._shared.errors.not_found import NotFoundError
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface
from src.classroom.usecases.get_activity_by_classroom_usecase_dto import OutputGetActivityByClassroomDto


class GetActivityByClassroomUsecase(UsecaseInterface):

    def __init__(self, repository: ActivityRepositoryInterface):
        self.repository = repository


    def execute(self, classroom_id: str) -> OutputGetActivityByClassroomDto:
        data = self.repository.get_by_classroom(classroom_id=classroom_id)

        if not data:
            raise NotFoundError("No activity found")
        
        now = datetime.datetime.now()
        output = []

        list_activity_id_time_expired = []



        for element in data:
            if now > element.time and element.availability:
                list_activity_id_time_expired.append(element.id)
                problems = []
            elif not now > element.time and element.availability:
                problems = element.list_problem
            else:
                problems = []

            output.append(
                OutputGetActivityByClassroomDto(
                    availability=element.availability,
                    category=element.category,
                    classroom_id=element.classroom_id,
                    id=element.id,
                    problem=problems,
                    problem_id=element.problem_id,
                    problem_name=element.problem_name,
                    problem_slug=element.problem_slug,
                    time=element.time,
                )
                )
        

        self.repository.update_availabity(list_activity_id_time_expired)

        return output
