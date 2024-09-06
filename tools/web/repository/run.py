
import datetime
from io import StringIO
from src.problems.domain.entity.problem import Problem, PropsProblemType
from src.problems.domain.factory.problem_factory import ProblemFactory
from src.problems.domain.value_object.file import File
from src.problems.domain.value_object.list import ListProblem
from src.problems.domain.value_object.slug import Slug
from web.repository.problems.problem_repository import ProblemRepository


class FileProblem:
    filename: str
    file: any

file_content = "problem1\nproblem2\nproblem3"
file = StringIO(file_content)

FileProblem.filename = "test.txt"
FileProblem.file = file


file = FileProblem

file = File(file=file.file, name=file.filename)

file = ListProblem(file)
input = ProblemFactory.create(
    id="123",
    comentary="alecrin",
    list_name="lista teste",
    slug=Slug("lista teste"),
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now(),
    list_problem=file,
)

repo = ProblemRepository.create(input)
