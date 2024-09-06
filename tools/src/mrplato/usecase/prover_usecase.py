import datetime
import pickle
from uuid import uuid4
from src._shared import session
from src._shared.services.service_mrplato_interface import ServiceMrplatoInterface
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src._shared.session.mrplato_session_interface import MrplatoSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.mrplato.usecase.prover_usecase_dto import InputProverUsecaseDto, OutpuProverUsecaseDto
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface
from src.problems.usecase.get_list_problem_dto import OutputGetListProblemDto
from src.statistic.facade.statistic_facade_dto import InputRegisterResultActivityFacade
from src.statistic.facade.statistic_facade_interface import StatisticFacadeInterface
from web.sdk.mrplato.prover_dto import InputProverDto, OutputProverDto


class ProverUsecase(UsecaseInterface):
    
    def __init__(self, service: ServiceMrplatoInterface, session: MrplatoSessionInterface, statistic_facade: StatisticFacadeInterface):
        self.service = service
        self.session = session
        self.statistic_facade = statistic_facade





    async def execute(self, input: InputProverUsecaseDto, response) -> OutpuProverUsecaseDto:

        session_data: MrplatoSessionDto = await self.session.verify(session_key=input.session_key, response=response)
        problem = input.problem

        #add num attempt
        session_data.num_attempts += 1

        input_prover = InputProverDto(
            input_formula=input.input_formula,
            sel_rule=input.sel_rule,
            selected_proof_line_indexes=input.selected_proof_line_indexes,
            selection=input.selection,
            total_or_partial=input.total_or_partial,
            type_selected=input.type_selected,
        )


   
        prover_instance = pickle.loads(session_data.prover)
        prover: OutputProverDto = self.service.prover(prover_instance=prover_instance, data=input_prover, problem=problem)
        
        if prover.type_output == "PROVED" and input.user_status is False:
            solutions = self.service.get_solution_service(prover_instance=prover_instance)


            input_result = InputRegisterResultActivityFacade(
                activity_id=input.activity_id,
                classroom_id=input.classroom_id,
                id=str(uuid4()),
                num_atempet=session_data.num_attempts,
                num_backs=session_data.num_backs,
                num_errors=session_data.num_errors,
                problem_id=input.pb_index,
                solution=solutions,
                student_id=input.user_id,
                time=datetime.datetime.now() - session_data.timer,
            )
            self.statistic_facade.register_result_activity(input=input_result)
            

        serialized_instance = pickle.dumps(prover.prover_instance)
        session_data.prover = serialized_instance

        await self.session.update(session_key=session_data.id, data_session=session_data)

        output = OutpuProverUsecaseDto(
            lines=prover.lines,
            message=str(prover.message),
            type_output=str(prover.type_output)
        )
        return output