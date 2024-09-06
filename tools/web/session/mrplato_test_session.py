

from unittest import result
from unittest.mock import Mock
from uuid import uuid4
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from web.session.mrplato_session import MrplatoSession
import asyncio


async def create_mrplato_session_TEST():
    response = Mock()
    session = MrplatoSession()
    result = await session.create(response)

    assert isinstance(result, MrplatoSessionDto)
    print("create_mrplato_session_TEST: Ok")



def get_mrplato_session_TEST():
    session_key = uuid4()
    obj = MrplatoSessionDto(
        id=session_key,
        prover=Mock(),
        time_session=Mock()
    )
    session = Mock(spec=MrplatoSession)
    result = session.get.return_value = obj

    assert isinstance(result, MrplatoSessionDto)
    assert result.id == obj.id
    print("get_mrplato_session_TEST: Ok")




async def verify_session_key_none_mrplato_session_TEST():
    session_key = None
    session = MrplatoSession()
    response = Mock()
    result = await session.verify(session_key=session_key, response=response)
    assert isinstance(result, MrplatoSessionDto)
    print("verify_session_key_none_mrplato_session_TEST: Ok")




    

if __name__ == "__main__":
    asyncio.run(create_mrplato_session_TEST())
    get_mrplato_session_TEST()
    asyncio.run(verify_session_key_none_mrplato_session_TEST())