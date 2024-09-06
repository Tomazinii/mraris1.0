



import datetime
from unittest.mock import Mock
from src._shared.value_object.email import Email

from src.classroom.domain.entity.student import Student
from src.classroom.usecases.register_student_usecase import RegisterStudentUsecase
from src.classroom.usecases.register_student_usecase_dto import InputRegisterStudentUsecaseDto


def test_register_student_usecase():

    repository = Mock()
    account_facade = Mock()
    usecase = RegisterStudentUsecase(repository=repository, account_facade=account_facade)

    input = InputRegisterStudentUsecaseDto(
        created_at=datetime.datetime.now(),
        enrollment="123456",
        id="id",
        name="alecrin",
        updated_at=datetime.datetime.now(),
        password="password",
        username="alecrin",
        classroom_id="id",
        email="a@a.com",
        invite_id="invite_id",
    )

    student = Student(
        created_at=input.created_at,
        enrollment=input.enrollment,
        id=input.id,
        name=input.username,
        updated_at=input.updated_at
    )
    email = Email(input.email)
    student.set_email(email=email)

    account_facade.register.return_value = None
    repository.create.return_value = None


    result = usecase.execute(input=input)

    assert result is None