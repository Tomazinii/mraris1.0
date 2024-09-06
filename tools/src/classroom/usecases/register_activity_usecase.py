


import datetime
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.factory.activity_factory import ActivityFactory
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface
from src.classroom.usecases.register_activity_usecase_dto import InputRegisterActivityUsecaseDto
from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface


class RegisterActivityUsecase(UsecaseInterface):

    def __init__(self, repository: ActivityRepositoryInterface, problem_facade: ProblemFacadeInterface):
        self.repository = repository
        self.problem_facade = problem_facade

    
    def execute(self, input: InputRegisterActivityUsecaseDto):

        problem: OutputProblemFacadeDto = self.problem_facade.get_by_id(input.problem_id)

        activity = ActivityFactory.create(
            category=input.category,
            classroom_id=input.classroom_id,
            created_at=input.created_at,
            id=input.id,
            updated_at=datetime.datetime.now(),
            list_problem=problem.list_problem,
            problem_id=problem.id,
            problem_name=problem.list_name,
            problem_slug=problem.slug,
            time=input.time,
            availability=input.availability,
        )
        


        self.repository.create(activity)
