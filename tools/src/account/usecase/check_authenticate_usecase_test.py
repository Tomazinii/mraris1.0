

import datetime
from unittest.mock import AsyncMock, Mock
from uuid import uuid4
from src._shared.session.user_session_dto import UserSessionDto
from src.account.usecase.check_authenticate_usecase import CheckAuthenticateUsecase
import pytest

from src.account.usecase.check_authenticate_usecase_dto import OutputCheckAuthenticateUsecaseDto


@pytest.mark.asyncio
async def test_check_authenticate_success():

    session = AsyncMock()
    service = Mock()

    user_session = UserSessionDto(
        id=uuid4(),
        user_id="user_id",
        time_session=datetime.datetime.now(),
        token="token",
        token_key="token_key",
    )

    session.verify.return_value = user_session


    service.decode.return_value = {
            "user_id": "user",
            "email": "a@a.com",
            "username": "alecrin",
            "is_authenticated": "user_test.get_is_authenticated()"
        }

    usecase = CheckAuthenticateUsecase(service=service, session=session)
    session_key = "session"

    result = await usecase.execute(session_key=session_key)

    assert isinstance(result, OutputCheckAuthenticateUsecaseDto)
    assert result.is_authenticated == True
    assert result.data != None



@pytest.mark.asyncio
async def test_check_authenticate_fail():

    session = AsyncMock()
    service = Mock()

    user_session = UserSessionDto(
        id=uuid4(),
        user_id="user_id",
        time_session=datetime.datetime.now(),
        token="token",
        token_key="token_key",
    )

    session.verify.return_value = None

    usecase = CheckAuthenticateUsecase(service=service, session=session)
    session_key = None

    result = await usecase.execute(session_key=session_key)

    assert isinstance(result, OutputCheckAuthenticateUsecaseDto)
    assert result.is_authenticated == False
    assert result.data == None

