

from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src._shared.usecase.usecase_interface import UsecaseInterface


class RestartStatusMrplatoController(ControllerInterface):
    
    def __init__(self, usecase: UsecaseInterface):
        self.usecase = usecase

    async def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        data = kwargs["data"]
        await self.usecase.execute(data)

        output = HttpResponse(status_code=200, body={})
        return output