


import datetime
from unittest.mock import Mock
from src._shared.value_object.email import Email

from src.classroom.domain.entity.student import Student
from src.classroom.usecases.get_student_classroom_usecase import GetStudentUsecase


def test_get_student_classroom_usecase():
    
    repository = Mock()
    usecase = GetStudentUsecase(repository=repository)

    student = Student(
        created_at=datetime.datetime.now(),
        enrollment="123456",
        id="id",
        name="name",
        updated_at=datetime.datetime.now()
    )
    student.set_classroom_id("classroom")
    email = Email("a@a.com")
    student.set_email(email)

    repository.get_by_id.return_value = student

    result = usecase.execute("user_id")

    assert result.enrollment == "123456"
    assert result.classroom_id == "classroom"