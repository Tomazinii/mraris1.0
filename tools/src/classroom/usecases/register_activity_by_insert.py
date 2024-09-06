

import datetime
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.factory.activity_factory import ActivityFactory
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface
from src.classroom.usecases.register_activity_by_insert_dto import InputRegisterActivityByInsertUsecaseDto
from src.problems.domain.value_object.slug import Slug
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto


class RegisterActivityByInsertUsecase(UsecaseInterface):
    
    def __init__(self, problem_facade: ProblemFacadeInterface, repository: ActivityRepositoryInterface):
        self.problem_facade = problem_facade
        self.repository = repository


    def execute(self, input: InputRegisterActivityByInsertUsecaseDto):
        
        input_problem = InputRegisterListProblemDto(
            comentary=input.problem_comentary,
            created_at=input.problem_created_at,
            id=input.problem_id,
            list_name=input.problem_list_name,
            list_problem=input.problem_list_problem,
            updated_at=input.problem_updated_at
        )

        problem = self.problem_facade.register_problem(input_problem)
        lista_normalizada = [item for item in problem.list_problem]

        activity = ActivityFactory.create(
            category=input.category,
            classroom_id=input.classroom_id,
            created_at=input.created_at,
            id=input.id,
            updated_at=datetime.datetime.now(),
            list_problem=lista_normalizada,
            problem_id=input.problem_id,
            problem_name=input.problem_list_name,
            problem_slug=Slug(input.problem_list_name).get_slug(),
            time=input.time,
            availability=input.availability,
        )

        self.repository.create(activity)
