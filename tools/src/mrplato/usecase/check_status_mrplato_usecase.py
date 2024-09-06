

import pickle
from src._shared.services.service_mrplato_interface import ServiceMrplatoInterface
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src._shared.session.mrplato_session_interface import MrplatoSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.mrplato.usecase.check_status_mrplato_usecase_dto import  InputCheckStatusMrplatoUsecaseDto, OutputCheckStatusMrplatoUsecaseDto


class CheckStatusMrplatoUsecase(UsecaseInterface):

    def __init__(self, session: MrplatoSessionInterface, service: ServiceMrplatoInterface):
        self.session = session
        self.service = service

    async def execute(self, input: InputCheckStatusMrplatoUsecaseDto, response):

        session_data: MrplatoSessionDto = await self.session.verify(session_key=input.session_key, response=response)


        prover_instance = pickle.loads(session_data.prover)
        
        service = self.service.get_current_status_prover(prover_instance, input.problem)


        output = OutputCheckStatusMrplatoUsecaseDto(
            conclusion = service["conclusion"],
            new_lines = service["new_lines"],
            premisses = service["premisses"]
        )

        return output

