


from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src.mrplato.usecase.prover_usecase import ProverUsecase


class MrplatoController(ControllerInterface):

    def __init__(self, usecase: ProverUsecase):
        self.usecase = usecase


    async def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        response = kwargs["response"]
        data = kwargs["data"]
        usecase = await self.usecase.execute(input=data, response=response)
        
   
        output = HttpResponse(status_code=201, body={"data":usecase})
        return output
        