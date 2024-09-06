from src._shared.usecase.usecase_interface import UsecaseInterface
from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto, OutputRegisterListProblemDto
from src.statistic.facade.statistic_facade_dto import InputRegisterResultActivityFacade
from src.statistic.facade.statistic_facade_interface import StatisticFacadeInterface


class StatisticFacade(StatisticFacadeInterface):

    def __init__(self, register_result_activity_usecase: UsecaseInterface = None):
        self.register_result_activity_usecase = register_result_activity_usecase

    def register_result_activity(self, input: InputRegisterResultActivityFacade):
        result = self.register_result_activity_usecase.execute(input)
        return result