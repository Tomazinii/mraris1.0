

import datetime
from unittest.mock import AsyncMock, Mock
from src.account.domain.entity.user import User
from src.account.domain.factory.user_factory import UserFactory
from src.account.usecase.login_usecase import LoginUsecase
import pytest
from src.account.usecase.login_usecase_dto import InputLoginUsecase

@pytest.mark.asyncio
async def test_login_usecase():

    repository = Mock()
    service = Mock()
    session = AsyncMock()
    
    user_test = UserFactory.create(
        created_at=datetime.datetime.now(),
        email="alecrin@gmail.com",
        id="id",
        password="passowords",
        updated_at=datetime.datetime.now(),
        username="alecrin"
    )



    jwt_mock = Mock()
    jwt_secret = "jwt_secret"
    service.encode.return_value = (jwt_mock, jwt_secret)
    session.create.return_value = None

    repository.get_by_email.return_value = user_test

    input = InputLoginUsecase(
        email="alecrin@gmail.com",
        password="passowords",
    )

    usecase = LoginUsecase(repository=repository, service=service, session=session)
    response = Mock()
    result = await usecase.execute(input=input, response=response)

    assert result is None