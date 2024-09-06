


import datetime
from unittest.mock import Mock
from src.account.usecase.user_register_usecase import UserRegisterUsecase
from src.account.usecase.user_register_usecase_dto import InputUserRegisterUsecaseDto


def test_create_user_no_admin_usecase():
    repository = Mock()
    repository.check_register.return_value = False
    usecase = UserRegisterUsecase(repository=repository)

    input = InputUserRegisterUsecaseDto(
        created_at=datetime.datetime.now(),
        email="alecrin@gmail.com",
        id="test_Id",
        is_admin=False,
        password="password",
        updated_at=datetime.datetime.now(),
        username="alecrin"
    )
    result = usecase.execute(input)
    assert result is None

