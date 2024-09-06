

import datetime
from io import StringIO
from unittest.mock import Mock
from tools.src._shared.controller.https.http_response import HttpResponse
from tools.src._shared.repository.problem_repository_interface import ProblemRepositoryInterface
from tools.src.problems.domain.value_object.file import File
from tools.src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto
from tools.src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase
from tools.web.controllers.problems.register_problem_controller import RegisterProblemController

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = { "first_name": "meuTeste" }



class FileProblem:
    filename: str
    file: any

def test_register_problem_test():
    repository = Mock(spec=ProblemRepositoryInterface)
    usecase = RegisterProblemUsecase(repository_service=repository)
    register_controller = RegisterProblemController(usecase)
    request = HttpRequestMock()

    file_content = "problem1\nproblem2\nproblem3"
    file = StringIO(file_content)
   
    FileProblem.filename = "test.txt"
    FileProblem.file = file


    file = FileProblem
    created_at = datetime.datetime.now()
    data = InputRegisterListProblemDto(comentary="lista teste comentary",created_at=created_at, id="id", list_name="lista teste", list_problem=file,updated_at=created_at)
    response = register_controller.execute(request, data=data)


    assert response.status_code == 201
    assert response.body["data"] is not None
    assert response.body["file"] is not None