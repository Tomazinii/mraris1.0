from src._shared.usecase.usecase_interface import UsecaseInterface
from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto, OutputRegisterListProblemDto


class ProblemFacade(ProblemFacadeInterface):

    def __init__(self, get_by_id_usecase: UsecaseInterface, register_problem_by_insert_usecase: UsecaseInterface = None):
        self.get_by_id_usecase = get_by_id_usecase
        self.register_problem_by_insert_usecase = register_problem_by_insert_usecase

    def get_by_id(self, input: InputProblemFacadeDto) -> OutputProblemFacadeDto:

        result = self.get_by_id_usecase.execute(input)

        return result
    
    def register_problem(self, input: InputRegisterListProblemDto) -> OutputRegisterListProblemDto:
        result = self.register_problem_by_insert_usecase.execute(input)
        return result

