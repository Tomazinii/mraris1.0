

from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src._shared.usecase.usecase_interface import UsecaseInterface


class GetAllProblemsController(ControllerInterface):

    def __init__(self, usecase: UsecaseInterface):
        self.usecase = usecase

    def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        
        output = self.usecase.execute()
        response = HttpResponse(
            status_code=200,
            body={"data":output}
        )

        return response
        