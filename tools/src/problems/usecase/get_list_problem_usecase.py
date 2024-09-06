


from src._shared.repository.problem_repository_interface import ProblemRepositoryInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.problems.domain.entity.problem import Problem
from src.problems.usecase.get_list_problem_dto import OutputGetListProblemDto


class GetListProblemUsecase(UsecaseInterface):
    
    def __init__(self, repository: ProblemRepositoryInterface):
        self.repository = repository

    
    def execute(self, id) -> OutputGetListProblemDto:

        element: Problem = self.repository.get_by_id(id)


        output = OutputGetListProblemDto(
            comentary=element.get_comentary(),
            created_at=element.get_created_at(),
            updated_at=element.get_updated_at(),
            id=element.get_id(),
            list_name=element.get_list_name(),
            list_problem=element.get_list_problem(),
            slug=element.get_slug().get_slug()
        )


        return output