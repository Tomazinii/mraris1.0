

from typing import List
from src._shared.repository.problem_repository_interface import ProblemRepositoryInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.problems.domain.entity.problem import Problem
from src.problems.usecase.get_all_problem_usecase_dto import OutputGetAllProblemUsecaseDto


class GetAllProblemsUsecase(UsecaseInterface):

    def __init__(self, repository: ProblemRepositoryInterface):
        self.repository = repository

    def execute(self) -> OutputGetAllProblemUsecaseDto:
        problems = self.repository.get_all()


        output = OutputGetAllProblemUsecaseDto(
            problems=problems
        )
        return output