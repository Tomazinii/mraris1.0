


from unittest.mock import Mock
from urllib import request
from src.problems.usecase.delete_list_problem_usecase import DeleteProblemUsecase
from web.controllers.problems.delete_problem_controller import DeleteProblemController


def test_delete_problem_controller():
    repository = Mock()
    repository.delete.return_value = None
    usecase = DeleteProblemUsecase(repository=repository)
    controller = DeleteProblemController(usecase=usecase)
    id = "id"
    request = Mock()

    result = controller.execute(request, data=id)
    

    assert result.status_code == 200
    assert result.body["data"] is None