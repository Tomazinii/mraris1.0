

from unittest.mock import Mock
from src._shared.controller.https.http_response import HttpResponse

from web.controllers.mrplato.get_options_controller import GetOptionController


def test_get_options_controller():
    usecase = Mock()
    controller = GetOptionController(usecase=usecase)
    request = Mock()
    response = Mock()

    response = controller.execute(request, data="id_test", response=response)

    assert response.status_code == 200
    assert response.body["data"] is not None
    assert isinstance(response, HttpResponse)