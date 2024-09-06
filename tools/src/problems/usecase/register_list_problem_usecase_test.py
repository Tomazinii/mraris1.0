
import datetime
from io import StringIO
from typing import IO
from unittest.mock import Mock
from uuid import UUID
from tools.src.problems.domain.value_object.file import File

from tools.src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto, OutputRegisterListProblemDto
from tools.src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase


class RepositoryMock:

    def create(self, input):
        pass
    

class FileProblem:
    filename: str
    file: any

def test_register_problem_usecase():
    repository = Mock(spec=RepositoryMock)
    file_content = "problem1\nproblem2\nproblem3"
    file = StringIO(file_content)

    FileProblem.filename = "test.txt"
    FileProblem.file = file


    file = FileProblem

    created_at = datetime.datetime.now()

    input = InputRegisterListProblemDto(comentary="lista teste comentary",created_at=created_at, id="id", list_name="lista teste", list_problem=file,updated_at=created_at)
    usecase = RegisterProblemUsecase(repository)
    output: OutputRegisterListProblemDto = usecase.execute(input)

    assert output.comentary == "lista teste comentary"
    assert output.created_at == created_at
    assert output.slug == "lista-teste"
    assert output.list_name == "lista teste"


    