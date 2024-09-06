
from src.account.domain.value_object.password import Password


def test_create_valid_password():
    password = "azsxdcfvgb"
    password = Password(password=password)
    assert password.get_password() is not None


def test_create_invalid_password():
    password = "123"
    try:
        password = Password(password=password)
    except Exception as error:
        assert str(error) == "the password must be at least 8 characters"

def test_encripty_password():
    password = "azsxdcfvgb"
    password = Password(password=password)
    assert password.get_password() != password