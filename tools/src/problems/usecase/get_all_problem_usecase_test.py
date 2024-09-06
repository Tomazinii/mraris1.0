

import datetime
from unittest.mock import Mock

from src.problems.domain.factory.problem_factory import ProblemFactory
from src.problems.domain.value_object.slug import Slug
from src.problems.usecase.get_all_problem_usecase import GetAllProblemsUsecase
from src.problems.usecase.get_all_problem_usecase_dto import OutputGetAllProblemUsecaseDto


def test_get_all_problems_usecase():

    repository = Mock()
    usecase = GetAllProblemsUsecase(repository)
    problem1 = ProblemFactory.create(
        id="id_test",
        list_name="test name",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        comentary="comentary",
        slug=Slug("test name"),
        list_problem=["problem1", "problem2", "problem3"]

    )

    problem2 = ProblemFactory.create(
        id="id_test",
        list_name="test name",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        comentary="comentary",
        slug=Slug("test name"),
        list_problem=["problem1", "problem2", "problem3"]

    )
    repository.get_all.return_value = [problem1, problem2]

    result = usecase.execute()
    
    assert isinstance(result, OutputGetAllProblemUsecaseDto)