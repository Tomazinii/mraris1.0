

import datetime
from src.classroom.domain.entity.activity import Activity
from src.classroom.domain.factory.activity_factory import ActivityFactory
from src.classroom.domain.entity.problem import Problem

def test_activity_factory():


    factory = ActivityFactory.create(
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
        availability=True
    )


    assert isinstance(factory, Activity)
    assert isinstance(factory.get_problem(), Problem)