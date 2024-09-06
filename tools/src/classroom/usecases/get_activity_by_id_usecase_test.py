

import datetime
from unittest.mock import Mock

from src.classroom.domain.factory.activity_factory import ActivityFactory
from src.classroom.usecases.get_activity_by_id_usecase import GetActivityByIdUsecase
from src.classroom.usecases.get_activity_by_id_usecase_dto import OutputGetActivityByIdDto


def test_get_activity_by_id_success():

    repository = Mock()
    activity =  ActivityFactory.create(
        category="categories",
        classroom_id="test",
        created_at=datetime.datetime.now(),
        id="id",
        list_problem=["problem1", "problem2"],
        problem_id="problem1",
        problem_name="problem",
        problem_slug="problem",
        time=datetime.datetime.now() + datetime.timedelta(days=1),
        updated_at=datetime.datetime.now(),
        availability=True,
    )

    repository.get_by_id.return_value = activity

    usecase = GetActivityByIdUsecase(repository=repository)

    result: OutputGetActivityByIdDto = usecase.execute(activity_id="id")

    assert result.category == activity.get_category()
    assert result.classroom_id == activity.get_classroom()
    assert result.id == activity.get_id()
    assert result.problem == activity.get_problem().get_list_problem()
    assert result.time == activity.get_time()


