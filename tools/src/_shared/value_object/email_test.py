

from src._shared.value_object.email import Email


def test_valid_email_value_object():

    email = "alecrin@discente.ufg.br"
    value_object = Email(email=email)

    assert value_object.get_email() == email


def test_invalid_email_value_object():

    email = "alecrindiscente.ufg.br"

    try:
        value_object = Email(email=email)
    except Exception as error:
         assert str(error) == "Invalid email"


