from unittest.mock import AsyncMock, Mock
from uuid import uuid4
import pytest
from src._shared.session.user_session_dto import UserSessionDto

from src.account.usecase.change_password_usecase import ChangePasswordUsecase
from src.account.usecase.change_password_usecase_dto import InputChangePasswordDto

@pytest.mark.asyncio
async def test_change_valid_password():
    repository = Mock()
    session = AsyncMock()
    session.verify.return_value = Mock()
    repository.change_password.return_value = None
    usecase = ChangePasswordUsecase(repository=repository, session=session)

    input = InputChangePasswordDto(
        new_password="senhavalida",
        session_key=uuid4()
    )
    result = await usecase.execute(input=input)

    assert result is None

@pytest.mark.asyncio
async def test_change_invalid_password():
    repository = Mock()
    session = AsyncMock()
    session.verify.return_value = Mock()
    repository.change_password.return_value = None
    usecase = ChangePasswordUsecase(repository=repository, session=session)

    input = InputChangePasswordDto(
        new_password="senida",
        session_key=uuid4()
    )
    try:
        result = await usecase.execute(input=input)
    except Exception as error:
        assert error.message == "the password must be at least 8 characters"