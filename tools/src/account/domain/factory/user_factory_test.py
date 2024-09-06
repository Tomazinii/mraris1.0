


import datetime
from src.account.domain.entity.user import User
from src.account.domain.factory.user_factory import UserFactory


def test_user_factory():
    
    factory = UserFactory()
    user = factory.create(
        updated_at=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        email="alecrin@gmail.com",
        id="test_id",
        password="passwords",
        username="username",
    )

    assert isinstance(user, User)
