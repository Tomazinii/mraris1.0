
class Prover:
    variable = "variable"



import datetime
import pickle
from unittest.mock import AsyncMock, Mock
from uuid import uuid4
import pytest
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src.mrplato.usecase.prover_usecase import ProverUsecase
from src.mrplato.usecase.prover_usecase_dto import InputProverUsecaseDto
from src.problems.usecase.get_list_problem_dto import OutputGetListProblemDto
from web.sdk.mrplato.prover_dto import OutputProverDto

@pytest.mark.asyncio
async def test_prover_usecase():
    # Dados de entrada para o caso de uso
    input_data = InputProverUsecaseDto(
        session_key="test_session_key",
        list_index="480dca05-a13a-4ac7-a9cf-436268084385",
        pb_index=0,
        input_formula="test_input_formula",
        sel_rule="1",
        selected_proof_line_indexes=[1, 2, 3],
        selection=0,
        total_or_partial="total",
        type_selected="1"
    )

    # Mocks para as dependências do caso de uso
    mock_service = Mock()
    mock_session = AsyncMock()
    mock_problem_facade = Mock()



    mock_problem_facade.get_by_id.return_value =  OutputGetListProblemDto(
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



    output_prover = OutputProverDto(
        lines=[{"content":"content", "methods_used_info":"methods_used_info", "type":"type"}],
        message="message",
        prover_instance=prover_no_serializer,
        type_output="CREATED"
     )
    mock_service.prover.return_value = output_prover

    mock_session.verify.return_value = MrplatoSessionDto(
        id=uuid4(),
        prover=prover,
        time_session=datetime.datetime.now()
    )

    mock_session.update.return_value = None


    # Inicialização do caso de uso
    prover_usecase = ProverUsecase(
        service=mock_service,
        session=mock_session,
        problem_facade=mock_problem_facade
    )

    # Execução do caso de uso
    result = await prover_usecase.execute(input_data, response=None)

    # Verificações/assertivas dos resultados
    assert result.lines == output_prover.lines
    assert result.message == output_prover.message
    assert result.type_output == output_prover.type_output
    
