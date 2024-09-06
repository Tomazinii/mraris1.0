


from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src._shared.usecase.usecase_interface import UsecaseInterface


class LinkResetPasswordController(ControllerInterface):
    
    def __init__(self, usecase: UsecaseInterface):
        self.usecase = usecase

    def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:

        self.usecase.execute(kwargs["data"])

        response = HttpResponse(
            status_code=201,
            body={}
        )
        return response
