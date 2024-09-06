

import datetime
from unittest.mock import Mock
from src.classroom.usecases.register_classroom_usecase import RegisterClassroomUsecase

from src.classroom.usecases.register_classroom_usecase_dto import InputRegisterClassroomDto


def test_register_classroom():

    repository = Mock()
    repository.create.return_value = None
    usecase = RegisterClassroomUsecase(repository=repository)

    input = InputRegisterClassroomDto(
        class_name="classroom",
        created_at=datetime.datetime.now(),
        id="id",
        teacher_id="teacher",
        updated_at=datetime.datetime.now(),
        teacher_created=datetime.datetime.now(),
        teacher_email="teacher@example.com",
        teacher_name="teacher",
        teacher_updated=datetime.datetime.now(),
    )

    result = usecase.execute(input)

    assert result.class_name == "classroom"
    assert result.id == "id"
    assert result.teacher_name == "teacher"