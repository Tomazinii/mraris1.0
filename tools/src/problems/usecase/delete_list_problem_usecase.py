

from src._shared.usecase.usecase_interface import UsecaseInterface
from src._shared.repository.problem_repository_interface import ProblemRepositoryInterface



class DeleteProblemUsecase(UsecaseInterface):
    
    def __init__(self, repository: ProblemRepositoryInterface):
        self.repository = repository

    
    def execute(self, id: str):
        self.repository.delete(id)
        
