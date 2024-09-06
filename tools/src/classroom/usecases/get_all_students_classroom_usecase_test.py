


import datetime
from unittest.mock import Mock

from src._shared.value_object.email import Email
from src.classroom.domain.entity.student import Student
from src.classroom.usecases.get_all_students_classroom_usecase import GetAllStudentsClassroomUsecase
from src.classroom.usecases.get_all_students_classroom_usecase_dto import OutputGetAllStudentUsecaseDto


def test_get_all_students_classroom_usecase_success():

    repository = Mock()
    student1 = Student(
        created_at=datetime.datetime.now(),
        enrollment="123456789",
        id="123456789",
        name="Student",
        updated_at=datetime.datetime.now()
    )
    student1.set_email(Email("q@q.com"))

    student_list = [student1,student1]
    repository.get_all_by_classroom.return_value = student_list
    usecase = GetAllStudentsClassroomUsecase(repository=repository)

    result: OutputGetAllStudentUsecaseDto = usecase.execute(classroom_id="id")

    assert result[0].name == student1.get_name()
    assert result[0].enrollment == student1.get_enrollment()
    assert result[0].email == student1.get_email()