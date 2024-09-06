

import datetime
from unittest.mock import Mock

from src.classroom.facade.classroom_facade_dto import OutputGetActivityByIdFacadeDto, OutputGetClassroomByIdFacadeDto
from src.classroom.usecases.get_activity_by_classroom_usecase_dto import OutputGetActivityByClassroomDto
from src.classroom.usecases.get_student_classroom_usecase_dto import OutputGetStudentDto
from src.statistic.usecase.register_result_activity_usecase import RegisterResultActivityUsecase
from src.statistic.usecase.register_result_activity_usecase_dto import InputRegisterResultActivityUsecaseDto


def test_register_result_activity_usecase():

    repository = Mock()
    activity_facade = Mock()
    student_facade = Mock()

    repository.verify.return_value = True
    repository.create.return_value = None

    activity_facade.get_activity_by_id_method.return_value = OutputGetActivityByIdFacadeDto(
        category="exercises",
        classroom_id="student",
        id="id",
        problem=["problem","problem"],
        problem_name="problem",
        time=datetime.datetime.now(),
    )

    student_facade.get_student_by_id.return_value = OutputGetStudentDto(
        classroom_id="classroom_id",
        email="student@example.com",
        enrollment="123456",
        name="classroom",

    )

    usecase = RegisterResultActivityUsecase(repository=repository, activity_facade=activity_facade, student_facade=student_facade)

    input = InputRegisterResultActivityUsecaseDto(
        activity_id="activity_id",
        classroom_id="classroom_id",
        id="id",
        num_atempet=10,
        num_backs=0,
        num_errors=0,
        problem_id=0,
        student_id="student_id",
        time=datetime.datetime.now(),
        solution=["solutiom"]
    )
    result = usecase.execute(input)


    assert result is None