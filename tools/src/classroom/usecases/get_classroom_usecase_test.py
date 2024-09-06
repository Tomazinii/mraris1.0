

import datetime
from unittest.mock import Mock

from src.classroom.domain.entity.classroom import Classroom
from src.classroom.domain.entity.teacher import Teacher
from src.classroom.usecases.get_classroom_usecase import GetClassroomUsecase
from src.classroom.usecases.get_classroom_usecase_dto import ClassroomDto, OutputGetClassroomUsecaseDto


def test_get_classroom():

    teacher =Teacher(
        created_at=datetime.datetime.now(),
        id="teste_id",
        name="teacher",
        updated_at=datetime.datetime.now()
    )

    teacher.set_email("a@a.com")
    
    classroom1 = ClassroomDto(
        class_name="turma a",
        created_at=datetime.datetime.now(),
        id="teste_id",
        teacher_email="a@a.com",
        teacher_name="teacher",
    )
    classroom2 = ClassroomDto(
        class_name="turma b",
        created_at=datetime.datetime.now(),
        id="teste_id",
        teacher_email="a@a.com",
        teacher_name="teacher",
    )


    repository = Mock()

    repository.get.return_value = OutputGetClassroomUsecaseDto(
        classrooms = [classroom1, classroom2]
    )
    usecase = GetClassroomUsecase(repository=repository)
    teacher_id = "teste_id"
    result: OutputGetClassroomUsecaseDto = usecase.execute(teacher_id)
    assert result.classrooms.classrooms[0].class_name == "turma a"
    assert result.classrooms.classrooms[0].id == "teste_id"
    assert result.classrooms.classrooms[0].teacher_name== "teacher"