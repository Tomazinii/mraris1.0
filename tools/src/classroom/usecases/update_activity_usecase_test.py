


import datetime
from unittest.mock import Mock

from src.classroom.usecases.update_activity_usecase import UpdateActivityUsecase
from src.classroom.usecases.update_activity_usecase_dto import InputUpdateActivityUsecaseDto


def test_update_activity_usecase():

    repository = Mock()
    usecase = UpdateActivityUsecase(repository=repository)

    input = InputUpdateActivityUsecaseDto(
        activity_id="id",
        time= datetime.datetime.now(),
        category="exercises",
        availability = True
    )
    repository.update.return_value = None
    result = usecase.execute(input)

    assert result is None

