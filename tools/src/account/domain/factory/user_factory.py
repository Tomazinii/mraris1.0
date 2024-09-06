

from src._shared.value_object.email import Email
from src.account.domain.entity.user import User
from src.account.domain.value_object.password import Password


class UserFactory:

    @staticmethod
    def create(updated_at, created_at, id, username, email, password) -> User:

        user = User(
            created_at=created_at,
            username=username,
            id=id,
            updated_at=updated_at
        )
        email = Email(email=email)
        password = Password(password=password)

        user.set_password(password=password)
        user.set_email(email=email)

        return user

        