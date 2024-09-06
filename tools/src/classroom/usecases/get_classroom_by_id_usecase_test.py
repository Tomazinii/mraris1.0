

import datetime
from unittest.mock import Mock

from src.classroom.domain.factory.classroom_factory import ClassroomFactory
from src.classroom.usecases.get_classroom_by_id_usecase import GetClassroomByIdUsecase


def test_get_classroom_by_id_usecase_success():

    repository = Mock()
    classroom = ClassroomFactory.create(
        class_name="class",
        created_at=datetime.datetime.now(),
        id="id",
        teacher_created=datetime.datetime.now(),
        teacher_email="teacher@example.com",
        teacher_id="teacher",
        teacher_name="teacher",
        teacher_updated=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    repository.get_by_id.return_value = classroom
    usecase = GetClassroomByIdUsecase(repository=repository)

    result = usecase.execute(classroom_id="id")

    assert result.teacher_email == classroom.get_teacher().get_email()
    assert result.class_name == classroom.get_name_class()
    assert result.id == classroom.get_id()
    