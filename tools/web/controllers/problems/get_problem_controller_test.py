


from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase








import datetime
from io import StringIO
from unittest.mock import Mock

from src.problems.domain.entity.problem import Problem, PropsProblemType
from src.problems.domain.factory.problem_factory import ProblemFactory
from src.problems.domain.value_object.file import File
from src.problems.domain.value_object.list import ListProblem
from src.problems.domain.value_object.slug import Slug
from src.problems.usecase.get_list_problem_dto import OutputGetListProblemDto
from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase
from web.controllers.problems.get_problem_controller import GetProblemController


class RepositoryMock:

    def create(self, input):
        pass

    def get_by_id(self, id):
        return



def test_get_problem_controller():

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


    usecase = GetListProblemUsecase(repository=repository)
    controller = GetProblemController(usecase=usecase)
    request = Mock()

    response = controller.execute(request, data="id_test")
    
    assert response.status_code == 200
    assert response.body["data"] is not None
    assert response.body["file"] is not None