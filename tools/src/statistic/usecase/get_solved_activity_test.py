

from unittest.mock import Mock

from src.statistic.usecase.get_solved_activity_dto import InputGetSolvedActivityDto
from src.statistic.usecase.get_solved_activity_usecase import GetSolvedActivityUsecase

class data:
    problem_id = 1



def test_get_solved_activity():

    repository = Mock()

    data_list = [data, data]

    repository.get_solved_activity.return_value = data_list
    usecase = GetSolvedActivityUsecase(repository=repository)

    activity_id = "activity_id"
    user_id = "user_id"

    input = InputGetSolvedActivityDto(
        activity_id=activity_id, 
        user_id=user_id
    )
    

    result = usecase.execute(input)

    assert result.activity_id == activity_id
    assert result.list_of_resolved_ativity