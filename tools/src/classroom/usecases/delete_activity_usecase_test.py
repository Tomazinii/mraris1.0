

from unittest.mock import Mock

from src.classroom.usecases.delete_activity_usecase import DeleteActivityUsecase


def test_delete_activity_usecase():

    repository = Mock()
    repository.delete.return_value = None
    usecase = DeleteActivityUsecase(repository=repository)

    activity_id = "id"
    result = usecase.execute(activity_id)

    assert result is None