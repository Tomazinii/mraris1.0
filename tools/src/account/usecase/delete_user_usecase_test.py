


from unittest.mock import Mock
from src.account.usecase.delete_user_usecase import DeleteUserUsecase


def test_delete_user():

    repository = Mock()
    repository.delete.return_value = None
    usecase = DeleteUserUsecase(repository=repository)
    result = usecase.execute(id="test-Id")

    assert result is None