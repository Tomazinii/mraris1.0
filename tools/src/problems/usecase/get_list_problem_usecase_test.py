




import datetime
from unittest.mock import Mock

from src.problems.domain.factory.problem_factory import ProblemFactory
from src.problems.domain.value_object.slug import Slug
from src.problems.usecase.get_list_problem_dto import OutputGetListProblemDto
from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase


class RepositoryMock:

    def create(self, input):
        pass

    def get_by_id(self, id):
        return
    
def test_get_list_problem():

    repository = Mock(spec=RepositoryMock)
    
    problem = ProblemFactory.create(
        id="id_test",
        list_name="test name",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        comentary="comentary",
        slug=Slug("test name"),
        list_problem=["problem1", "problem2", "problem3"]

    )

    repository.get_by_id.return_value = problem

    usecase = GetListProblemUsecase(repository)

    id = problem.get_id()
    result:OutputGetListProblemDto = usecase.execute(id)

    assert result.comentary == problem.get_comentary()
    assert result.list_name == problem.get_list_name()
    assert result.list_problem == problem.get_list_problem()


