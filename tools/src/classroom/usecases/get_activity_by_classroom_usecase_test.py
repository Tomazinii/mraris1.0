


import datetime
from unittest.mock import Mock
from src.classroom.usecases.get_activity_by_classroom_usecase import GetActivityByClassroomUsecase

from src.classroom.usecases.get_activity_by_classroom_usecase_dto import OutputGetActivityByClassroomDto



def test_get_activity_usecase():

    repository = Mock()
    usecase = GetActivityByClassroomUsecase(repository=repository)

    activity = OutputGetActivityByClassroomDto(
        availability=True,
        problem=["list"],
        category="category",
        classroom_id="id",
        id="id",
        problem_id="id",
        problem_name="problem",
        problem_slug="slug",
        time=datetime.datetime.now(),

    )

    repository.get_by_classroom.return_value = activity

    result = usecase.execute("id")

    assert result.availability == True
    assert result.category == "category"
    assert result.classroom_id == "id"
    assert result.problem_name == "problem"
