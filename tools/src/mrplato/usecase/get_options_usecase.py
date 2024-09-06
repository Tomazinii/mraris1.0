import pickle
from src._shared.services.service_mrplato_interface import ServiceMrplatoInterface
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src._shared.session.mrplato_session_interface import MrplatoSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.mrplato.usecase.get_options_usecase_dto import InputGetOptionsUsecaseDto, OutputGetOptionsUsecaseDto
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface
from src.problems.usecase.get_list_problem_dto import OutputGetListProblemDto
from web.sdk.mrplato.get_options_dto import InputGetOptionDto, OutputGetOptionDto


class GetOptionsUsecase(UsecaseInterface):

    def __init__(self, service: ServiceMrplatoInterface, session: MrplatoSessionInterface):
        self.service = service
        self.session = session

    async def execute(self, input: InputGetOptionsUsecaseDto, response) -> OutputGetOptionsUsecaseDto:

        session_data: MrplatoSessionDto = await self.session.verify(input.session_key, response=response)

        input_get_option = InputGetOptionDto(
            sel_rule=input.sel_rule,
            selected_proof_line_indexes=input.selected_proof_line_indexes,
            session_key=input.session_key,
            total_or_partial=input.total_or_partial,
            type_selected=input.type_selected,
        )

        prover_instance = pickle.loads(session_data.prover)

        get_option: OutputGetOptionDto = self.service.get_option(prover_instance=prover_instance, data=input_get_option, problem=input.problem)

        serialized_instance = pickle.dumps(get_option.prover_instance)

        session_data.prover = serialized_instance

        await self.session.update(session_key=session_data.id, data_session=session_data)
        
        output = OutputGetOptionsUsecaseDto(
            lines=get_option.lines,
            message=get_option.message,
            type_output=get_option.type_output
        )

        return output

