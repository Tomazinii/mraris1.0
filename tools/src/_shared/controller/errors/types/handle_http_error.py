
from src._shared.controller.https.http_response import HttpResponse
from src._shared.errors.bad_request import BadRequestError
from src._shared.errors.forbidden import ForbiddenError
from src._shared.errors.not_found import NotFoundError
from src._shared.errors.unauthorized import UnauthorizedError


def handle_errors(error: Exception) -> HttpResponse:

    if(isinstance(error, BadRequestError)):
        return HttpResponse(
            status_code=400,
            body=error
        )
    
    if(isinstance(error, NotFoundError)):
        return HttpResponse(
            status_code=404,
            body=error
    )

    if(isinstance(error, UnauthorizedError)):
        return HttpResponse(
            status_code=401,
            body=error
    )

    if(isinstance(error, ForbiddenError)):
        return HttpResponse(
            status_code=403,
            body=error
        )


    return HttpResponse(
        status_code=500,
        body=error
    )