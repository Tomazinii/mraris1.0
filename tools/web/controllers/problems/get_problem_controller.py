

from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase


class GetProblemController(ControllerInterface):

    def __init__(self, usecase: GetListProblemUsecase):
        self.usecase = usecase


    def execute(self, request: HttpRequest, **kwargs ) -> HttpResponse:

        output = self.usecase.execute(kwargs["data"])
        file = output.list_problem
        output.list_problem = None

        response = HttpResponse(
            status_code=200,
            body={"data":output, "file":file}
        )

        return response
        