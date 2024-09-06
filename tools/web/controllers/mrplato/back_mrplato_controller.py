

from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src._shared.usecase.usecase_interface import UsecaseInterface


class BackStateMrplatoController(ControllerInterface):
    def __init__(self, usecase: UsecaseInterface):
        self.usecase = usecase

    async def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        response = kwargs["response"]
        data = kwargs["data"]

        output = await self.usecase.execute(input=data,response=response)

        return HttpResponse(
            status_code=201,
              body={"data":output}
        )