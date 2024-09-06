
from unittest.mock import Mock

from src.problems.usecase.delete_list_problem_usecase import DeleteProblemUsecase




class RepositoryMock:

    def create(self, input):
        pass

    def delete(self, id):
        return

def test_delete_list_problem():
    repository = Mock(spec=RepositoryMock)
    repository.delete.return_value = None

    usecase = DeleteProblemUsecase(repository)
    id = "id"
    result = usecase.execute(id)

    assert result is None