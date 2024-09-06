




import datetime
import pickle
from unittest.mock import AsyncMock, Mock
from uuid import uuid4
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src.mrplato.usecase.get_options_usecase import GetOptionsUsecase

from src.mrplato.usecase.get_options_usecase_dto import InputGetOptionsUsecaseDto, OutputGetOptionsUsecaseDto
from src.problems.usecase.get_list_problem_dto import OutputGetListProblemDto
from web.sdk.mrplato.get_options_dto import OutputGetOptionDto

import pytest

class Prover:
    variable = "variable"


@pytest.mark.asyncio
async def test_get_options_usecase():
    input = InputGetOptionsUsecaseDto(
        list_index="teste",
        pb_index=0,
        sel_rule="1",
        selected_proof_line_indexes=[0,1],
        session_key="session_key",
        type_selected="1"
    )

    session = AsyncMock()
    service = Mock()
    problem_facade = Mock()

    problem_facade.get_by_id.return_value = OutputGetListProblemDto(
         comentary="teste",
         created_at=datetime.datetime.now(),
         id="session_key",
         list_name="list name",
         list_problem=["problema 1", "problema 2"],
         slug="list-name",
         updated_at=datetime.datetime.now(),
     )

    prover_no_serializer = Prover()
    prover = pickle.dumps(prover_no_serializer)
    

    output_get_option = OutputGetOptionDto(
        lines=[{"content": "content", "type":"CREEATE", "methods_used_info": "create"}],
        message="message",
        prover_instance=prover_no_serializer,
        type_output="CREATED"
    )
    service.get_option.return_value = output_get_option
    session.verify.return_value =  MrplatoSessionDto(
        id=uuid4(),
        prover=prover,
        time_session=datetime.datetime.now()
    )
    session.update.return_value = None
    usecase = GetOptionsUsecase(session=session, service=service,problem_facade=problem_facade)
    response = Mock()
    result: OutputGetOptionsUsecaseDto = await usecase.execute(input,response=response)

    assert result.lines == output_get_option.lines
    assert result.message == output_get_option.message
    assert result.type_output == output_get_option.type_output
    assert isinstance(result, OutputGetOptionsUsecaseDto)
