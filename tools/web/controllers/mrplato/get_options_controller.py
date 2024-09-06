

from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src.mrplato.usecase.get_options_usecase import GetOptionsUsecase


class GetOptionController(ControllerInterface):

    def __init__(self, usecase: GetOptionsUsecase):
        self.usecase = usecase

    async def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:

        response = kwargs["response"]
        data = kwargs["data"]

        output = await self.usecase.execute(input=data,response=response)

        return HttpResponse(
            status_code=200,
              body={"data":output}
        )