
from abc import ABC, abstractmethod

from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto, OutputRegisterListProblemDto


class ProblemFacadeInterface(ABC):

    @abstractmethod
    def get_by_id(self, input: InputProblemFacadeDto) -> OutputProblemFacadeDto:
        raise NotImplementedError
    
    @abstractmethod
    def register_problem(self, input: InputRegisterListProblemDto) -> OutputRegisterListProblemDto:
        raise NotImplementedError
