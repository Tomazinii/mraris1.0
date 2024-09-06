


import pickle
from src._shared.services.service_mrplato_interface import ServiceMrplatoInterface
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src._shared.session.mrplato_session_interface import MrplatoSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.mrplato.usecase.back_mrplato_usecase_dto import InputBackMrplatoUsecaseDto, OutputBackMrplatoUsecaseDto



class BackMrplatoUsecase(UsecaseInterface):

    def __init__(self, session: MrplatoSessionInterface, service_back_mrplato: ServiceMrplatoInterface):
        self.session = session
        self.service = service_back_mrplato


    async def execute(self, input: InputBackMrplatoUsecaseDto, response) -> OutputBackMrplatoUsecaseDto:

        session_data: MrplatoSessionDto = await self.session.verify(session_key=input.session_key, response=response)

        prover_instance = pickle.loads(session_data.prover)


        service = self.service.back_state_mrplato(prover_instance)

        prover = pickle.dumps(service["prover_instance"])

        session_data.prover = prover
        session_data.num_backs += 1
        await self.session.update(input.session_key, session_data)


        output = OutputBackMrplatoUsecaseDto(
            conclusion = service["conclusion"],
            new_lines = service["new_lines"],
            premisses = service["premisses"]
        )
        
        return output





