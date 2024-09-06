
from abc import ABC, abstractmethod

from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        pass