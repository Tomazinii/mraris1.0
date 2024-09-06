
from unittest.mock import AsyncMock
from uuid import uuid4
from src.account.usecase.logout_usecase import LogoutUsecase
import pytest


@pytest.mark.asyncio
async def test_logout_usecase():
    session = AsyncMock()
    session.delete.return_value =  None
    usecase = LogoutUsecase(session=session)
    session_key = uuid4()
    result = await usecase.execute(session_key=session_key)

    assert result is None