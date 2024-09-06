

import datetime
from unittest.mock import Mock
from src.classroom.usecases.register_activity_usecase import RegisterActivityUsecase
from src.classroom.usecases.register_activity_usecase_dto import InputRegisterActivityUsecaseDto
from src.problems.facade.problem_facade_dto import OutputProblemFacadeDto


def test_register_activity():

    repository = Mock()
    problem_facade = Mock()

    repository.create.return_value = None

    problem_facade.get_by_id.return_value = OutputProblemFacadeDto(
        comentary="comentary",
        created_at=datetime.datetime.now(),
        id="id",
        list_name="lista",
        list_problem=["problem", "problem"],
        slug="slug",
        updated_at=datetime.datetime.now(),
    )
    

    usecase = RegisterActivityUsecase(repository=repository, problem_facade=problem_facade)

    input = InputRegisterActivityUsecaseDto(
        category="category",
        classroom_id="classroom",
        created_at=datetime.datetime.now(),
        id="id",
        problem_id="problem_id",
        time=datetime.datetime.now(),
    )
    result = usecase.execute(input=input)


    assert result is None